
import streamlit as st
from datetime import datetime

# Helper function to reduce a number to a single digit or master number
def reduce_number(n):
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(d) for d in str(n))
    return n

# Generate all jersey numbers and HR totals that reduce to the target number
def get_matching_numbers(target_day):
    return [i for i in range(1, 100) if reduce_number(i) == target_day]

# Generate all MM/DD birthdays that reduce to the target number
def get_matching_birthdays(target_day):
    matches = []
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                if reduce_number(month + day) == target_day:
                    matches.append(f"{month:02d}/{day:02d}")
            except:
                continue
    return matches

# Layout
st.title("🔢 Numerology Sports Sync Tool")
st.write("Enter a date to find synced jersey #s, HR milestones, and birthdays:")

# Date input
input_date = st.date_input("Select a date:", value=datetime.today())

# Trigger processing
if st.button("Calculate Numerology"):
    year = input_date.year
    month = input_date.month
    day = input_date.day

    # Universal numbers
    universal_year = reduce_number(sum(int(d) for d in str(year)))
    universal_month = reduce_number(month + universal_year)
    universal_day = reduce_number(universal_month + day)

    related_numbers = get_matching_numbers(universal_day)
    matching_birthdays = get_matching_birthdays(universal_day)

    # Results
    st.subheader("🔮 Numerology Breakdown")
    st.markdown(f"**Universal Year:** {universal_year}")
    st.markdown(f"**Universal Month:** {universal_month}")
    st.markdown(f"**Universal Day:** {universal_day}")

    st.subheader("🎽 Jersey & HR Numbers That Match")
    st.write(", ".join(str(n) for n in related_numbers))

    st.subheader("🎂 Birthdays That Match (MM/DD)")
    st.write(", ".join(matching_birthdays))
