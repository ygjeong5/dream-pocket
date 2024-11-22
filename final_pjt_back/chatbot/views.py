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
                f"- {product.fin_prdt_nm} (by {product.kor_co_nm})\n"
                f"  • 최고금리: {max_rate}%\n"
                f"  • 가입기간: {', '.join(set(str(opt.save_trm) + '개월' for opt in options))}\n"
                f"  • 특징: {product.etc_note}"
            )
        
        product_info_str = "\n".join(product_info)

        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        
        messages = [
            {"role": "system", "content": f"""당신은 친절한 금융 전문 상담사입니다.

• 현재 추천 가능한 금융상품 TOP5:
{product_info_str}

• 상담 가이드라인:
1. 고객 필요 분석
   - 저축 목적 (주택마련, 결혼자금 등)
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

• 주의사항:
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
        return Response({'response': response})
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def chat_message(request):
#     message = request.data.get('message')
#     try:
#         # 키워드 기반 응답 시스템
#         if "주식" in message:
#             response = "주식 투자에 대한 조언입니다:\n1. 장기 투자를 권장합니다\n2. 분산 투자로 리스크를 관리하세요\n3. 시장 상황을 주기적으로 모니터링하세요"
#         elif "적금" in message or "예금" in message:
#             response = "현재 은행 금리 상황을 고려할 때:\n1. 단기 예금보다는 장기 적금이 유리합니다\n2. 현재 시중은행 평균 금리는 3~4% 수준입니다\n3. 특판 상품을 활용하면 더 높은 금리를 받을 수 있습니다"
#         elif "펀드" in message:
#             response = "펀드 투자 시 고려사항:\n1. 자신의 투자 성향을 파악하세요\n2. 분산 투자가 중요합니다\n3. 수수료와 환매 조건을 꼭 확인하세요"
#         elif "대출" in message:
#             response = "대출 관련 조언:\n1. 신용점수에 따라 금리가 달라집니다\n2. 고정금리와 변동금리의 장단점을 비교해보세요\n3. 중도상환수수료를 확인하세요"
#         elif "투자" in message:
#             response = "투자 전략 조언:\n1. 분산 투자로 리스크를 관리하세요\n2. 정기적인 투자를 통해 평균단가를 낮추세요\n3. 장기적인 관점에서 접근하세요"
#         elif "연금" in message:
#             response = "연금 관련 조언:\n1. 국민연금은 기본입니다\n2. 퇴직연금을 적극 활용하세요\n3. 개인연금으로 추가 대비가 필요합니다"
#         else:
#             response = "구체적인 금융 관련 키워드(예: 주식, 펀드, 적금, 대출, 투자, 연금)를 포함하여 질문해 주시면 더 자세한 답변을 드릴 수 있습니다."
            
#         return Response({'response': response})
    
#     except Exception as e:
#         return Response({'error': str(e)}, status=500)