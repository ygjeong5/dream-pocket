from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from openai import OpenAI
from django.conf import settings
from finlife.models import FinancialProducts, FinancialOptions


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat_message(request):
    message = request.data.get('message')
    try:
        # DB에서 금융상품 정보 가져오기
        products = FinancialProducts.objects.all()
        
        # 금융상품 정보 문자열로 변환
        product_info = []
        for product in products[:5]:  # 상위 5개 상품
            options = FinancialOptions.objects.filter(product=product.id)
            max_rate = max([opt.intr_rate2 for opt in options if opt.intr_rate2 != -1], default=0)
            product_info.append(
                f"### {product.fin_prdt_nm} *(by {product.kor_co_nm})*\n"
                f"- **최고금리**: {max_rate}%\n"
                f"- **가입기간**: {', '.join(set(str(opt.save_trm) + '개월' for opt in options))}\n"
                f"- **특징**: {product.etc_note or '정보 없음'}"
            )
        
        product_info_str = "\n\n".join(product_info)

        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        
        messages = [
            {"role": "system", "content": f"""당신은 친절한 금융 전문 상담사입니다.

### 현재 추천 가능한 금융상품 TOP5:
{product_info_str}

#### 상담 가이드라인:
1. 고객 필요 분석
   - 저축 목적 (예: 주택마련, 결혼자금 등)
   - 가입 희망 기간
   - 선호 은행
   - 월 저축 가능 금액
   
2. 맞춤형 상품 추천
   - 위 상품 중 최적의 상품 추천
   - 금리 조건 상세 설명
   - 가입 기간별 예상 수익 계산
   - 가입 방법 안내

3. 답변 스타일
   - 친절하고 쉬운 설명
   - 구체적인 수치 제시
   - 단계별 안내

#### 주의사항:
- 실제 DB에 있는 상품만 추천
- 정확한 금리 정보 제공
- 은행명과 상품명 정확히 안내
- 각 상품의 특이사항 설명"""},
            {"role": "user", "content": message}
        ]

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )

        response = completion.choices[0].message.content

        # 마크다운 형식을 JSON으로 반환
        return Response({'response': response})
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)
