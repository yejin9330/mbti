import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🌸 MBTI 꽃 추천",
    page_icon="🌺",
    layout="centered"
)

# CSS 스타일링
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Nanum Gothic', sans-serif;
    }
    
    .main {
        background-color: #fff9fb;
    }
    
    .title-box {
        background: linear-gradient(135deg, #ffb7c5, #ffd6e0, #c8e6c9);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(255, 183, 197, 0.4);
    }
    
    .result-box {
        background: linear-gradient(135deg, #fff0f5, #f0fff4);
        border: 2px solid #ffb7c5;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 4px 20px rgba(255, 183, 197, 0.3);
    }
    
    .flower-emoji {
        font-size: 80px;
        margin: 10px;
    }
    
    .mbti-badge {
        background: linear-gradient(135deg, #ff8fab, #fb6f92);
        color: white;
        padding: 8px 20px;
        border-radius: 50px;
        font-size: 22px;
        font-weight: bold;
        display: inline-block;
        margin: 10px;
        box-shadow: 0 3px 10px rgba(251, 111, 146, 0.4);
    }
    
    .flower-name {
        font-size: 32px;
        font-weight: 800;
        color: #d63384;
        margin: 10px 0;
    }
    
    .flower-desc {
        font-size: 16px;
        color: #666;
        line-height: 1.8;
        margin: 10px 0;
    }
    
    .keyword-box {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 8px;
        margin: 15px 0;
    }
    
    .keyword {
        background-color: #ffe0eb;
        color: #c9184a;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
    }
    
    .fun-fact {
        background-color: #fff8dc;
        border-left: 4px solid #ffd700;
        border-radius: 10px;
        padding: 15px 20px;
        margin-top: 15px;
        text-align: left;
        font-size: 15px;
        color: #555;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #ff8fab, #fb6f92);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 50px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(251, 111, 146, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(251, 111, 146, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# MBTI 꽃 데이터
mbti_flowers = {
    "INTJ": {
        "flower": "검은 장미 🖤🌹",
        "emoji": "🖤🌹🔮",
        "name": "블랙 로즈 (Black Rose)",
        "keywords": ["신비로운", "완벽주의", "독립적", "전략적"],
        "description": (
            "희귀하고 신비로운 블랙 로즈처럼, INTJ는 남들과는 다른 독특한 매력을 가지고 있어요. "
            "완벽을 추구하는 당신은 어두운 장미처럼 신비롭고 강렬한 존재감을 뿜어냅니다! "
            "혼자만의 시간을 소중히 여기며 깊은 사고를 즐기는 당신에게 딱이에요. 🌟"
        ),
        "fun_fact": "💡 재미있는 사실: 블랙 로즈는 사실 완전한 검정색이 아니라 매우 진한 보라색이에요! "
                   "겉으로 보이는 것 이상의 깊이를 가진 INTJ와 꼭 닮았죠? 🔮",
        "color": "#1a0533",
        "bg_color": "#f5e6ff"
    },
    "INTP": {
        "flower": "파란 수국 💙🌸",
        "emoji": "💙🌸🔬",
        "name": "블루 수국 (Blue Hydrangea)",
        "keywords": ["지적인", "분석적", "호기심 많은", "창의적"],
        "description": (
            "수국은 토양의 산도에 따라 색이 변하는 신기한 꽃이에요! 🧪 "
            "지식을 탐구하며 끊임없이 변화하는 INTP처럼, 수국도 환경에 따라 다양하게 변신해요. "
            "복잡한 아이디어를 즐기는 당신에게 이 신비로운 꽃을 선물할게요! 📚"
        ),
        "fun_fact": "💡 재미있는 사실: 수국꽃 하나처럼 보이는 것은 사실 수백 개의 작은 꽃들이 모인 거예요! "
                   "다양한 관심사를 가진 INTP와 완벽하게 매칭! 🌍",
        "color": "#1565c0",
        "bg_color": "#e3f2fd"
    },
    "ENTJ": {
        "flower": "빨간 장미 🌹❤️",
        "emoji": "🌹❤️👑",
        "name": "레드 로즈 (Red Rose)",
        "keywords": ["리더십", "카리스마", "야망 있는", "결단력"],
        "description": (
            "꽃의 여왕 빨간 장미처럼, ENTJ는 어디서든 주목받는 천생 리더예요! 👑 "
            "당당하고 강렬한 존재감으로 주변 사람들을 이끄는 당신. "
            "목표를 향해 거침없이 나아가는 모습이 빨간 장미의 당찬 아름다움과 꼭 닮았어요! 🔥"
        ),
        "fun_fact": "💡 재미있는 사실: 빨간 장미는 전 세계에서 가장 많이 재배되는 꽃으로 "
                   "로마 시대부터 권력과 승리의 상징이었어요! 역시 ENTJ답죠? 🏆",
        "color": "#c62828",
        "bg_color": "#ffebee"
    },
    "ENTP": {
        "flower": "해바라기 🌻✨",
        "emoji": "🌻✨💡",
        "name": "선플라워 (Sunflower)",
        "keywords": ["활발한", "창의적", "논쟁 좋아함", "도전적"],
        "description": (
            "항상 밝은 빛을 향해 고개를 드는 해바라기처럼, ENTP는 새로운 아이디어와 도전을 사랑해요! 💡 "
            "토론을 즐기고 창의적인 발상으로 주변을 놀라게 하는 당신. "
            "해바라기의 눈부신 에너지가 딱 당신의 것이에요! ☀️"
        ),
        "fun_fact": "💡 재미있는 사실: 해바라기의 씨앗은 피보나치 수열로 배열되어 있어요! "
                   "수학적 패턴을 즐기는 ENTP라면 이 사실에 흥분할 것 같은데요? 🤓",
        "color": "#f57f17",
        "bg_color": "#fffde7"
    },
    "INFJ": {
        "flower": "라벤더 💜🌿",
        "emoji": "💜🌿🌙",
        "name": "라벤더 (Lavender)",
        "keywords": ["통찰력 있는", "이상주의적", "공감 능력 높은", "신비로운"],
        "description": (
            "은은한 향기로 사람들의 마음을 치유하는 라벤더처럼, INFJ는 깊은 공감 능력으로 "
            "주변 사람들에게 평화와 위로를 선물해요. 🌙 "
            "희귀하고 특별한 당신의 존재감은 라벤더의 특별한 보라빛과 닮았어요! 💫"
        ),
        "fun_fact": "💡 재미있는 사실: 라벤더는 불면증, 불안 완화에 효과가 있다고 해요! "
                   "주변 사람들의 마음을 치유하는 INFJ와 완벽한 매칭이죠? 🌸",
        "color": "#6a1b9a",
        "bg_color": "#f3e5f5"
    },
    "INFP": {
        "flower": "물망초 🩵🌼",
        "emoji": "🩵🌼🦋",
        "name": "포겟미낫 (Forget-me-not)",
        "keywords": ["감성적인", "이상주의적", "창의적", "진정성 있는"],
        "description": (
            "작지만 특별한 아름다움을 가진 물망초처럼, INFP는 겉으론 조용하지만 "
            "내면에 풍부한 감성과 깊은 가치관을 가지고 있어요. 🦋 "
            "'나를 잊지 말아요'라는 꽃말처럼, 한번 만나면 잊을 수 없는 특별한 사람이에요! 💙"
        ),
        "fun_fact": "💡 재미있는 사실: 물망초의 영어 이름 'Forget-me-not'은 독일 전설에서 유래했어요! "
                   "낭만적인 이야기를 사랑하는 INFP에게 딱 어울리는 꽃이죠? 📖",
        "color": "#0277bd",
        "bg_color": "#e1f5fe"
    },
    "ENFJ": {
        "flower": "튤립 🌷🌈",
        "emoji": "🌷🌈🤗",
        "name": "레인보우 튤립 (Rainbow Tulip)",
        "keywords": ["따뜻한", "카리스마 있는", "배려심 깊은", "영감을 주는"],
        "description": (
            "다양한 색으로 피어나는 튤립처럼, ENFJ는 모든 사람을 포용하고 이해하는 "
            "따뜻한 마음을 가지고 있어요! 🌈 "
            "사람들에게 영감을 주고 이끌어가는 당신은 봄날 만개한 튤립처럼 "
            "세상을 밝게 만드는 존재예요! 🤗"
        ),
        "fun_fact": "💡 재미있는 사실: 튤립은 원래 중앙아시아가 원산지인데, 네덜란드의 상징이 되었어요! "
                   "어디서든 적응하고 빛을 발하는 ENFJ와 닮지 않았나요? ✈️",
        "color": "#e91e63",
        "bg_color": "#fce4ec"
    },
    "ENFP": {
        "flower": "해당화 🌺🎉",
        "emoji": "🌺🎉🦄",
        "name": "와일드 로즈 (Wild Rose)",
        "keywords": ["열정적인", "자유로운", "창의적", "사교적인"],
        "description": (
            "야생에서 자유롭게 피어나는 야생 장미처럼, ENFP는 어디서든 자신만의 빛깔로 "
            "화려하게 꽃피워요! 🦄 "
            "새로운 사람과 아이디어에 열정적으로 반응하는 당신의 에너지는 "
            "들판을 가득 채우는 야생화처럼 넘실거려요! 🎉"
        ),
        "fun_fact": "💡 재미있는 사실: 야생 장미는 가시가 있어 보호받지만 꽃은 무척 아름다워요! "
                   "자유롭지만 자신만의 기준이 확실한 ENFP와 꼭 닮았네요! 🌟",
        "color": "#e91e63",
        "bg_color": "#fff0f5"
    },
    "ISTJ": {
        "flower": "국화 🌼📚",
        "emoji": "🌼📚⚖️",
        "name": "크리산테멈 (Chrysanthemum)",
        "keywords": ["성실한", "책임감 있는", "꼼꼼한", "신뢰할 수 있는"],
        "description": (
            "오랫동안 변치 않고 아름다움을 유지하는 국화처럼, ISTJ는 언제나 믿을 수 있는 "
            "든든한 존재예요! ⚖️ "
            "책임감 있게 맡은 일을 완수하고 원칙을 중요시하는 당신에게 "
            "절개와 성실함의 꽃 국화를 드려요! 🌟"
        ),
        "fun_fact": "💡 재미있는 사실: 국화는 동아시아에서 수천 년간 재배되어온 꽃으로 "
                   "장수와 행복의 상징이에요! 오래가는 신뢰를 주는 ISTJ와 완벽 매칭! ⭐",
        "color": "#f57f17",
        "bg_color": "#fff8e1"
    },
    "ISFJ": {
        "flower": "은방울꽃 🔔🤍",
        "emoji": "🔔🤍🏡",
        "name": "릴리 오브 더 밸리 (Lily of the Valley)",
        "keywords": ["헌신적인", "따뜻한", "배려심 깊은", "겸손한"],
        "description": (
            "작고 순수한 은방울꽃처럼, ISFJ는 조용하지만 깊은 사랑으로 주변을 보살펴요. 🏡 "
            "소중한 사람들을 위해 묵묵히 헌신하는 당신의 모습은 "
            "숲속에서 은은하게 향기를 풍기는 은방울꽃과 꼭 닮았어요! 💕"
        ),
        "fun_fact": "💡 재미있는 사실: 은방울꽃은 '행복이 돌아온다'는 꽃말을 가지고 있어요! "
                   "주변 사람들에게 행복을 가져다주는 ISFJ에게 딱 맞는 꽃이죠? 😊",
        "color": "#2e7d32",
        "bg_color": "#e8f5e9"
    },
    "ESTJ": {
        "flower": "카네이션 🌹💪",
        "emoji": "🌹💪📋",
        "name": "레드 카네이션 (Red Carnation)",
        "keywords": ["체계적인", "리더십", "실용적인", "추진력 있는"],
        "description": (
            "강인하고 오래 피어있는 카네이션처럼, ESTJ는 어떤 상황에서도 흔들리지 않는 "
            "강한 의지와 실행력을 가지고 있어요! 💪 "
            "규칙과 질서를 중요시하고 책임감 있게 조직을 이끄는 당신에게 "
            "힘과 사랑의 꽃 카네이션을 드려요! 📋"
        ),
        "fun_fact": "💡 재미있는 사실: 카네이션은 약 2000년의 재배 역사를 가진 꽃으로 "
                   "어떤 환경에서도 잘 자라요! 강한 추진력의 ESTJ와 완벽 매칭! 💫",
        "color": "#b71c1c",
        "bg_color": "#ffebee"
    },
    "ESFJ": {
        "flower": "해바라기 🌻💛",
        "emoji": "🌻💛🤝",
        "name": "미모사 (Mimosa)",
        "keywords": ["사교적인", "배려심 깊은", "협동적", "따뜻한"],
        "description": (
            "노란 미모사꽃처럼 주변을 환하게 밝히는 ESFJ! 🌞 "
            "사람들과의 관계를 소중히 여기고 언제나 따뜻한 미소로 주변을 행복하게 만드는 당신. "
            "사교적이고 배려심 깊은 당신에게 밝고 따뜻한 미모사를 선물해요! 💛"
        ),
        "fun_fact": "💡 재미있는 사실: 미모사는 '섬세한 감정', '우정'을 의미해요! "
                   "인간관계를 소중히 여기는 ESFJ에게 이보다 어울리는 꽃이 있을까요? 🤝",
        "color": "#f9a825",
        "bg_color": "#fffde7"
    },
    "ISTP": {
        "flower": "선인장 꽃 🌵🌸",
        "emoji": "🌵🌸🔧",
        "name": "카투스 플라워 (Cactus Flower)",
        "keywords": ["독립적인", "실용적인", "과묵한", "손재주 있는"],
        "description": (
            "거친 환경에서도 아름다운 꽃을 피우는 선인장처럼, ISTP는 어떤 상황에서도 "
            "냉정하고 유연하게 해결책을 찾아내요! 🔧 "
            "겉으로는 가시가 있어 보이지만 내면에는 아름다운 꽃을 품고 있는 당신, "
            "진정한 매력이 숨어있는 타입이에요! 💎"
        ),
        "fun_fact": "💡 재미있는 사실: 선인장 꽃은 일 년에 단 하루만 피는 종류도 있어요! "
                   "자신을 쉽게 드러내지 않는 ISTP와 완벽하게 닮았네요! 🌟",
        "color": "#2e7d32",
        "bg_color": "#f1f8e9"
    },
    "ISFP": {
        "flower": "벚꽃 🌸💗",
        "emoji": "🌸💗🎨",
        "name": "체리 블라썸 (Cherry Blossom)",
        "keywords": ["예술적인", "자유로운", "온화한", "감성적인"],
        "description": (
            "잠깐이지만 눈부시게 아름다운 벚꽃처럼, ISFP는 순간의 아름다움을 가장 잘 느끼고 "
            "표현하는 예술적인 영혼이에요! 🎨 "
            "조용하지만 독자적인 예술 감각으로 세상을 아름답게 만드는 당신, "
            "바로 봄의 주인공이에요! 🌸"
        ),
        "fun_fact": "💡 재미있는 사실: 벚꽃이 피는 기간은 고작 1-2주에 불과해요! "
                   "그 짧은 순간이기에 더욱 아름다운 것처럼, 현재를 사는 ISFP와 완벽 매칭! ✨",
        "color": "#e91e63",
        "bg_color": "#fce4ec"
    },
    "ESTP": {
        "flower": "파이어 릴리 🔥🌺",
        "emoji": "🔥🌺⚡",
        "name": "파이어 릴리 (Fire Lily)",
        "keywords": ["활동적인", "대담한", "현실적인", "스릴을 즐기는"],
        "description": (
            "강렬하고 눈에 확 들어오는 파이어 릴리처럼, ESTP는 어디서든 주목받는 "
            "에너지 넘치는 존재예요! ⚡ "
            "위기 상황에서 빛나고 모험을 즐기는 당신의 역동적인 매력은 "
            "불꽃처럼 타오르는 파이어 릴리와 꼭 닮았어요! 🔥"
        ),
        "fun_fact": "💡 재미있는 사실: 파이어 릴리는 산불 이후에 더욱 활발하게 피어나요! "
                   "위기에서 오히려 강해지는 ESTP와 완벽한 매칭이네요! 💪",
        "color": "#bf360c",
        "bg_color": "#fbe9e7"
    },
    "ESFP": {
        "flower": "거베라 데이지 🌼🎊",
        "emoji": "🌼🎊🎤",
        "name": "거베라 데이지 (Gerbera Daisy)",
        "keywords": ["활발한", "낙천적인", "재미있는", "즉흥적인"],
        "description": (
            "알록달록 다양한 색깔로 피어나는 거베라 데이지처럼, ESFP는 어디서든 "
            "분위기를 띄우고 즐거움을 가져다주는 존재예요! 🎉 "
            "삶을 파티처럼 즐기고 모든 순간을 무대로 만드는 당신, "
            "밝고 화려한 거베라가 딱이에요! 🎤"
        ),
        "fun_fact": "💡 재미있는 사실: 거베라는 세계에서 5번째로 많이 팔리는 꽃이에요! "
                   "인기 많고 사랑받는 ESFP에게 완벽하게 어울리는 꽃이죠? ⭐",
        "color": "#ff6f00",
        "bg_color": "#fff8e1"
    },
}

# 메인 앱
def main():
    # 타이틀
    st.markdown("""
        <div class="title-box">
            <h1>🌸 MBTI 꽃 추천 🌸</h1>
            <p style="font-size: 18px; color: #555; margin: 0;">
                나의 MBTI에 어울리는 꽃은 무엇일까요? 🤔💐
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # 소개 문구
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🌺 16가지 꽃")
        st.markdown("<p style='text-align:center; color:#888;'>각 MBTI에 딱 맞는 특별한 꽃이 있어요!</p>", unsafe_allow_html=True)
    with col2:
        st.markdown("### 🔍 꽃말 분석")
        st.markdown("<p style='text-align:center; color:#888;'>꽃말과 성격을 연결해드려요!</p>", unsafe_allow_html=True)
    with col3:
        st.markdown("### 💡 재미있는 사실")
        st.markdown("<p style='text-align:center; color:#888;'>꽃에 관한 신기한 이야기도 있어요!</p>", unsafe_allow_html=True)

    st.markdown("---")

    # MBTI 선택
    st.markdown("### 🌟 나의 MBTI를 선택해보세요!")

    mbti_list = list(mbti_flowers.keys())

    # 4x4 그리드로 버튼 표시
    cols = st.columns(4)
    selected_mbti = None

    # selectbox로 선택
    selected_mbti = st.selectbox(
        "MBTI 유형을 선택하세요 👇",
        ["선택해주세요 💭"] + mbti_list,
        index=0
    )

    st.markdown("")

    # 결과 표시
    if selected_mbti and selected_mbti != "선택해주세요 💭":
        data = mbti_flowers[selected_mbti]

        # 풍선 효과
        if st.button("✨ 꽃 추천 받기! ✨"):
            st.balloons()

        st.markdown(f"""
            <div class="result-box">
                <div class="flower-emoji">{data['emoji']}</div>
                <div class="mbti-badge">✨ {selected_mbti} ✨</div>
                <div class="flower-name">🌸 {data['name']} 🌸</div>
                
                <div class="keyword-box">
                    {"".join([f'<span class="keyword">#{kw}</span>' for kw in data["keywords"]])}
                </div>
                
                <div class="flower-desc">{data['description']}</div>
                
                <div class="fun-fact">{data['fun_fact']}</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        st.markdown(f"""
            <p style='text-align:center; color:#aaa; font-size:14px;'>
                🌸 친구에게 공유하고 친구의 꽃도 알아보세요! 🌸
            </p>
        """, unsafe_allow_html=True)

    else:
        # 선택 전 안내
        st.markdown("""
            <div style='text-align:center; padding: 40px; color: #ccc;'>
                <div style='font-size: 60px;'>💐</div>
                <p style='font-size: 18px;'>위에서 MBTI를 선택하면<br>당신에게 어울리는 꽃을 알려드려요! 🌸</p>
            </div>
        """, unsafe_allow_html=True)

    # 하단 모든 MBTI 미리보기
    st.markdown("---")
    st.markdown("### 🌺 모든 MBTI 꽃 미리보기")
    
    preview_cols = st.columns(4)
    for i, (mbti, data) in enumerate(mbti_flowers.items()):
        with preview_cols[i % 4]:
            st.markdown(f"""
                <div style='
                    background: {data["bg_color"]};
                    border-radius: 15px;
                    padding: 15px;
                    text-align: center;
                    margin: 5px 0;
                    border: 1px solid #eee;
                '>
                    <div style='font-size: 24px;'>{data["emoji"].split()[0]}</div>
                    <div style='font-weight: bold; color: {data["color"]}; font-size: 14px;'>{mbti}</div>
                    <div style='font-size: 12px; color: #888;'>{data["flower"]}</div>
                </div>
            """, unsafe_allow_html=True)

    # 푸터
    st.markdown("")
    st.markdown("""
        <div style='text-align:center; padding: 20px; color: #ccc; font-size: 13px;'>
            🌸 Made with 💕 and Streamlit 🌸<br>
            당곡고등학교 AI 도우미
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
