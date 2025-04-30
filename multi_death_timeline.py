
import streamlit as st

# Simulated list of death events with timestamps and reasons
death_events = [
    {
        "timestamp": "00:34",
        "reason": "You ego peeked mid without holding TPP. Enemy pre-aimed and out-reacted you.",
        "sensitivity": {
            "Camera": 60,
            "ADS": 60,
            "Gyro": 215,
            "Gyro ADS": 200
        },
        "recommended": {
            "Camera": 65,
            "ADS": 55,
            "Gyro": 230,
            "Gyro ADS": 250
        }
    },
    {
        "timestamp": "01:47",
        "reason": "Crosshair was too low. You aimed at the waist while enemy headshot you.",
        "sensitivity": {
            "Camera": 62,
            "ADS": 58,
            "Gyro": 210,
            "Gyro ADS": 190
        },
        "recommended": {
            "Camera": 65,
            "ADS": 55,
            "Gyro": 225,
            "Gyro ADS": 240
        }
    },
    {
        "timestamp": "02:58",
        "reason": "You went prone in open. Reduced reaction time and spray delay caused your death.",
        "sensitivity": {
            "Camera": 60,
            "ADS": 60,
            "Gyro": 215,
            "Gyro ADS": 200
        },
        "recommended": {
            "Camera": 65,
            "ADS": 55,
            "Gyro": 230,
            "Gyro ADS": 250
        }
    }
]

def multi_death_timeline():
    st.title("🧠 AimPro AI – Multi-Death Timeline")

    for i, event in enumerate(death_events, start=1):
        st.markdown(f"## 💀 Death {i} – {event['timestamp']}")
        st.warning(event["reason"])

        st.markdown("**🎯 Estimated Sensitivity:**")
        st.code("\n".join([f"{k}: {v}" for k, v in event["sensitivity"].items()]), language="yaml")

        st.markdown("**🛠️ Recommended Sensitivity:**")
        st.code("\n".join([f"{k}: {v}" for k, v in event["recommended"].items()]), language="yaml")

        st.markdown("---")

if __name__ == "__main__":
    multi_death_timeline()
