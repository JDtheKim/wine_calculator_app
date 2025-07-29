import streamlit as st

# 설정
st.set_page_config(page_title="와인 양조 계산기", layout="centered")
st.title("🍷 와인 양조 계산기")

# -----------------------------------
# SECTION 1: 당도 계산기
# -----------------------------------
st.header("📈 브릭스 당도 계산기")

sugar_types = {
    "백설탕 (100%)": 1.00,
    "꿀 (79%)": 0.79,
    "포도당 시럽 (70%)": 0.70
}

with st.form("brix_form"):
    col1, col2 = st.columns(2)
    with col1:
        volume_l = st.number_input("기준 용액의 양 (L)", min_value=0.0, value=1.0, step=0.1)
        current_brix = st.number_input("현재 브릭스 (°Bx)", min_value=0.0, value=10.0, step=0.1)
    with col2:
        target_brix = st.number_input("목표 브릭스 (°Bx)", min_value=0.0, value=12.0, step=0.1)
        sugar_type = st.selectbox("당류 종류", options=list(sugar_types.keys()))
    
    submitted_brix = st.form_submit_button("당류 계산")

if submitted_brix:
    solution_mass = volume_l * 1000
    current_sugar_g = solution_mass * current_brix / 100
    target_sugar_g = solution_mass * target_brix / 100
    sugar_needed = target_sugar_g - current_sugar_g
    sugar_ratio = sugar_types[sugar_type]
    actual_sugar_to_add = sugar_needed / sugar_ratio

    st.success(f"✅ {sugar_type} 기준으로 추가해야 할 양: **{actual_sugar_to_add:.2f} g**")

# -----------------------------------
# SECTION 2: 첨가제 계산기
# -----------------------------------
st.header("⚗️ 첨가제 자동 계산기")

with st.form("additive_form"):
    additive_volume = st.number_input("총 용액의 양 (L)", min_value=0.0, value=20.0, step=1.0)
    submitted_additives = st.form_submit_button("첨가제 계산")

if submitted_additives:
    so2 = additive_volume * 0.1    # 아황산염
    yeast = additive_volume * 0.2
    dap = additive_volume * 0.3
    sorbate = additive_volume * 0.2

    st.markdown("### 💊 권장 투입량")
    st.markdown(f"🧪 **아황산염 (KMS)**: `{so2:.2f} g`")
    st.markdown(f"🍞 **효모**: `{yeast:.2f} g`")
    st.markdown(f"🧬 **제2인산암모늄 (DAP)**: `{dap:.2f} g`")
    st.markdown(f"🔒 **소르빈산염**: `{sorbate:.2f} g`")

# -----------------------------------
st.caption("🔧 참고: 기준값은 일반적인 홈브루잉 가이드 기준으로 계산됨.")
