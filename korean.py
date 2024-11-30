import streamlit as st

# Streamlit 앱 설정
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap');
        
        body {{
            background-color: #f8f9fa;
            font-family: 'Nanum Gothic', sans-serif;
            color: #2c3e50;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            padding: 2em;
            margin: 0 auto;
            width: 90%;
            max-width: 1200px;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }}
        .section {{
            background-color: #fff9c4;
            padding: 20px;
            border-radius: 8px;
            margin: 15px 0;
            font-size: 1.1em;
            color: #2c3e50;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            line-height: 1.6;
        }}
        .info-header {{
            background: #e3f2fd;
            color: #1565c0;
            padding: 15px 20px;
            border-radius: 8px;
            margin: 10px 0;
            font-weight: 600;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }}
        .category-title {{
            color: #1565c0;
            padding: 15px;
            margin: 15px 0;
            border-bottom: 2px solid #90caf9;
            font-weight: 600;
        }}
        .stButton button {{
            background: #ffffff;
            color: #1565c0;
            padding: 12px 20px;
            border-radius: 8px;
            border: 1px solid #90caf9;
            margin: 8px 0;
            width: 100%;
            transition: all 0.2s ease;
            font-size: 1em;
        }}
        .stButton button:hover {{
            background: #e3f2fd;
            border-color: #1565c0;
        }}
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            background-color: #ffffff;
            border-radius: 8px;
            padding: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }}
        .stTabs [data-baseweb="tab"] {{
            background-color: transparent;
            color: #1565c0;
            border-radius: 6px;
            padding: 10px 20px;
            font-weight: 600;
        }}
        .stTabs [aria-selected="true"] {{
            background: #e3f2fd;
            color: #1565c0;
        }}
    </style>
""", unsafe_allow_html=True)

st.title("제주도 음식을 소개합니다!")

# 세션 상태 초기화
if 'active_specialty' not in st.session_state:
    st.session_state.active_specialty = None
if 'active_local' not in st.session_state:
    st.session_state.active_local = None

# 특산물 정보 딕셔너리
specialties = {
    "감귤": {
        "desc": "알칼리성 식품으로 다이어트에 좋으며, 칼슘의 흡수를 도와준다. 신진대사를 원활히 하며, 비타민C가 풍부하여 피부미용과 피로회복에 좋다.",
        "image": "images/a.jpg"
    },
    "고사리": {
        "desc": "단백질, 섬유소, 칼슘, 칼륨 등 각종 무기질이 풍부하다. 추자굴비, 제주 돼지고기와 특히 궁합이 잘 맞는 음식으로 찌개, 무침, 육개장 등으로 요리한다.",
        "image": "images/b.jpg"
    },
    "자리돔": {
        "desc": "5~8월이 제철로 물회, 강회, 구이, 젓갈, 조림 등으로 요리된다. 열량이 낮아 비만인 사람에게 적합하며, 맛이 담백하고 기름기가 적어 소화가 용이하여 병후 회복기 환자에게 좋다.",
        "image": "images/c.jpg"
    },
    "옥돔": {
        "desc": "조선시대부터 왕실 진상품으로 올려졌다. 살은 단단하고 지방이 적고 단백질은 풍부하다. 칼슘, 인, 철분 등의 미네랄과 비타민 A, B1, B2 성분이 풍부하다.",
        "image": "images/d.jpg"
    },
    "갈치": {
        "desc": "9~10월이 제철로 살이 희고 부드러우며, 다이어트 식사에 활용 및 어린이 성장발육촉진에 좋다. 조림, 호박국, 구이, 튀김 등으로 요리한다.",
        "image": "images/e.jpg"
    },
    "말고기": {
        "desc": "풍병이나 몸 가려움에 좋다하여 약용으로 이용 되었으며, 다리뼈는 관절염, 신경통의 특효약이다. 어린이에게는 감기예방에 탁월하다.",
        "image": "images/f.jpg"
    },
    "흑돼지고기": {
        "desc": "제주 돼지는 거의 모든 부위를 이용하여 요리에 사용한다. 육질이 뛰어나고 비계 양이 적어서 맛이 월등히 좋다.",
        "image": "images/g.jpg"
    }
}

# 향토 음식 정보 딕셔너리
local_foods = {
    "자리돔물회": {
        "desc": "자리돔물회는 제주도에서 여름철에 즐기는 냉국 대용으로, 회를 떠서 무친 다음 물을 부어 먹는다 해서 물회라는 이름이 붙여졌다.",
        "image": "images/h.jpg"
    },
    "갈치국": {
        "desc": "갈치국은 토막 낸 싱싱한 갈치에다 호박, 얼갈이배추, 풋고추를 넣어 소금간을 해 만든 국이다.",
        "image": "images/i.jpg"
    },
    "성게국": {
        "desc": "싱싱한 미역과 함께 끓인 성게국은 잔치나 상례 등 경조사에 성게국을 끓여 손님에게 접대하는 하는 일이 보편적이다.",
        "image": "images/j.jpg"
    },
    "한치물회": {
        "desc": "여름철 어느 식당에서나 가장 큰 인기를 누리며 자리돔물회와 함께 양대 산맥을 이룬다.",
        "image": "images/k.jpg"
    },
    "옥돔구이": {
        "desc": "도미의 여왕이라 불리는 옥돔을 배를 갈라 소금을 뿌려 꾸덕꾸덕하게 말린 뒤 구운 것으로 담백한 맛이 일품이다.",
        "image": "images/l.jpg"
    },
    "빙떡": {
        "desc": "빙떡은 삶은 무채로 만든 소를 메밀 전병으로 말아 만든 떡이다. 메밀 전의 담백한 맛과 무채의 삼삼하고 시원한 맛이 어우러져 독특한 맛이 난다.",
        "image": "images/m.jpg"
    },
    "고기국수": {
        "desc": "고기국수는 마을의 잔칫날이나 큰 행사가 있던 날 즐겨먹던 음식이다.",
        "image": "images/n.jpg"
    }
}

# 탭 선택
tab1, tab2 = st.tabs(["제주 7대 특산물", "제주 7대 향토음식"])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("<div class='category-title'>특산물 선택</div>", unsafe_allow_html=True)
        for item in specialties.keys():
            if st.button(item, key=f"specialty_{item}", use_container_width=True):
                st.session_state.active_specialty = item if st.session_state.active_specialty != item else None
    
    with col2:
        st.markdown("<div class='info-header'>정보 (누른 음식 버튼을 한번 더 누르면 정보가 숨겨집니다.)</div>", unsafe_allow_html=True)
        if st.session_state.active_specialty:
            st.markdown(f"<div class='section'>{specialties[st.session_state.active_specialty]['desc']}</div>", unsafe_allow_html=True)
            try:
                st.image(specialties[st.session_state.active_specialty]['image'], 
                        caption=f"제주 {st.session_state.active_specialty}", 
                        use_column_width=True)
            except:
                st.info("이미지 준비중입니다")

with tab2:
    col3, col4 = st.columns([1, 2])
    with col3:
        st.markdown("<div class='category-title'>향토음식 선택</div>", unsafe_allow_html=True)
        for item in local_foods.keys():
            if st.button(item, key=f"local_{item}", use_container_width=True):
                st.session_state.active_local = item if st.session_state.active_local != item else None
    
    with col4:
        st.markdown("<div class='info-header'>정보 (누른 음식 버튼을 한번 더 누르면 정보가 숨겨집니다.)</div>", unsafe_allow_html=True)
        if st.session_state.active_local:
            st.markdown(f"<div class='section'>{local_foods[st.session_state.active_local]['desc']}</div>", unsafe_allow_html=True)
            try:
                st.image(local_foods[st.session_state.active_local]['image'], 
                        caption=f"제주 {st.session_state.active_local}", 
                        use_column_width=True)
            except:
                st.info("이미지 준비중입니다")