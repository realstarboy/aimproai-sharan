
import streamlit as st

def death_reason_screen():
    st.title("🧠 AimPro AI: Death Analysis Report")

    st.markdown("### 🎥 Clip Summary")
    st.write("🕒 Detected Death at: **2.00s**")
    st.write("🎮 Gun Used: M416")
    st.write("🔍 Scope: Red Dot")
    st.write("📍 Map: TDM - Warehouse")

    st.markdown("### ❌ Reason for Death")
    st.warning(
        "**You went prone mid-fight**, which drastically reduced your movement speed and made you a static target.\n"
        "The enemy, likely standing and ready, out-reacted you."
    )

    st.markdown("### ✅ What You Should Have Done")
    st.success(
        "- Use a **quick crouch spray or strafe peek** instead of going prone.\n"
        "- **Pre-aim** the enemy’s location and hold crosshair at chest level.\n"
        "- In TDM, avoid prone unless you're catching enemies off guard from cover."
    )

    st.markdown("### 🎯 Detected Sensitivity (Estimated from Gameplay)")
    st.code("Camera: 60\nADS: 60\nGyro: 215", language="yaml")

    st.markdown("### 🛠️ Recommended Sensitivity (For Your Style)")
    st.code("Camera: 65\nADS: 55\nGyro: 230", language="yaml")
    st.caption("⚙️ Increased Gyro for faster vertical control. Lowered ADS to reduce overshoot. Boosted Camera for TPP shoulder aim.")

    st.markdown("---")
    st.info("💡 Pro Tip: Your playstyle is mid-range aggressive. Balance speed with recoil control using the above sensitivity.")

if __name__ == "__main__":
    death_reason_screen()
