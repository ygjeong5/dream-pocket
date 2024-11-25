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
        for product in products[:5]:  # 상위 3개 상품
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommend(request):
    try:
        user_input = request.data.get('message', {})
        
        # 사용자 입력값 추출
        age = user_input.get('age', '20대')
        period = user_input.get('period', '6개월')
        amount = user_input.get('amount', 50)
        purpose = user_input.get('purpose', '비상금')
        preferential_conditions = user_input.get('preferential_conditions', '')

        # DB에서 금융상품 정보 가져오기
        products = FinancialProducts.objects.all()
        
        # 금융상품 정보 문자열로 변환
        product_info = []
        for product in products[:5]:
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

### 고객 정보:
- 연령대: {age}
- 가입희망기간: {period}
- 월 저축 가능액: {amount}만원
- 저축 목적: {purpose}
- 우대조건: {preferential_conditions}

#### 응답 형식:
다음 형식으로 응답해주세요:

### 고객 분석
[고객의 연령대, 저축 목적, 우대조건 등을 고려한 간단한 분석]

### 추천 상품 TOP3
1. [상품명] (은행명)
   - 최고금리: [금리]%
   - 가입기간: [기간]
   - 월 저축금액: [금액]만원
   - 예상 수익: [수익금액]
   - 특징: [상품 특징]

2. [다음 상품 정보...]

3. [다음 상품 정보...]

### 추천 이유
[왜 이 상품들을 추천하는지 설명]

### 가입 방법
[구체적인 가입 절차 안내]

### 주의사항
[가입 시 주의할 점이나 우대금리 조건 등]"""},
            {"role": "user", "content": f"제 나이는 {age}이고, {period} 동안 매월 {amount}만원을 {purpose}을 위해 저축하고 싶습니다. 우대조건은 {preferential_conditions}입니다. 어떤 상품이 좋을까요?"}
        ]

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )

        response = completion.choices[0].message.content

        # 마크다운 형식으로 응답 변환
        formatted_response = response.replace(
            "### ", "\n\n### "
        ).replace(
            "1. ", "\n\n1. "
        ).replace(
            "2. ", "\n\n2. "
        ).replace(
            "3. ", "\n\n3. "
        ).replace(
            "- ", "\n- "
        )

        return Response({'response': formatted_response})
    
    except Exception as e:
        print(f"Error in recommend view: {str(e)}")
        return Response({'error': str(e)}, status=500)

