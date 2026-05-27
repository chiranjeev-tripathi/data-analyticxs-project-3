# ==========================================
# E-COMMERCE ANALYTICS + CHURN PREDICTION
# COMPLETE FIXED STREAMLIT APP
# ==========================================

# =============== IMPORT LIBRARIES =================

import streamlit as st
import pandas as pd
import pickle
import os

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="E-Commerce Analytics System",
    layout="wide"
)

# ==========================================
# LOAD PIPELINE
# ==========================================

pipeline = pickle.load(
    open("churn_pipeline.pkl", "rb")
)

# ==========================================
# TITLE
# ==========================================

st.title("E-Commerce Customer Analytics System")

st.write(
    "Analytics + Customer Churn Prediction Dashboard"
)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Customer Churn Prediction"
    ]
)

# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":

    st.header("Business Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Revenue",
            "$1.2M"
        )

    with col2:
        st.metric(
            "Customers",
            "10,000"
        )

    with col3:
        st.metric(
            "Churn Rate",
            "12%"
        )

    with col4:
        st.metric(
            "Retention Rate",
            "88%"
        )

    st.subheader("Project Features")

    st.write("""
    ✅ Customer Analytics  
    ✅ Churn Prediction  
    ✅ Business Insights  
    ✅ AI Integration Ready  
    ✅ Real-Time Predictions  
    """)

# ==========================================
# CHURN PREDICTION PAGE
# ==========================================

elif page == "Customer Churn Prediction":

    st.header("Customer Churn Prediction")

    st.write(
        "Enter Customer Details"
    )

    # ==========================================
    # INPUT COLUMNS
    # ==========================================

    col1, col2 = st.columns(2)

    # ==========================================
    # COLUMN 1
    # ==========================================

    with col1:

        Age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=35
        )

        Gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        Membership_Years = st.number_input(
            "Membership Years",
            min_value=0,
            max_value=20,
            value=3
        )

        Login_Frequency = st.number_input(
            "Login Frequency",
            min_value=0,
            max_value=100,
            value=15
        )

        Session_Duration_Avg = st.number_input(
            "Session Duration Avg",
            min_value=0.0,
            value=45.0
        )

        Pages_Per_Session = st.number_input(
            "Pages Per Session",
            min_value=0,
            value=6
        )

        Cart_Abandonment_Rate = st.slider(
            "Cart Abandonment Rate",
            0.0,
            1.0,
            0.2
        )

        Wishlist_Items = st.number_input(
            "Wishlist Items",
            min_value=0,
            value=4
        )

        Total_Purchases = st.number_input(
            "Total Purchases",
            min_value=0,
            value=20
        )

        Average_Order_Value = st.number_input(
            "Average Order Value",
            min_value=0.0,
            value=2500.0
        )

        Lifetime_Value = st.number_input(
            "Lifetime Value",
            min_value=0.0,
            value=5000.0
        )

    # ==========================================
    # COLUMN 2
    # ==========================================

    with col2:

        Days_Since_Last_Purchase = st.number_input(
            "Days Since Last Purchase",
            min_value=0,
            value=10
        )

        Discount_Usage_Rate = st.slider(
            "Discount Usage Rate",
            0.0,
            1.0,
            0.3
        )

        Returns_Rate = st.slider(
            "Returns Rate",
            0.0,
            1.0,
            0.1
        )

        Email_Open_Rate = st.slider(
            "Email Open Rate",
            0.0,
            1.0,
            0.5
        )

        Customer_Service_Calls = st.number_input(
            "Customer Service Calls",
            min_value=0,
            value=1
        )

        Product_Reviews_Written = st.number_input(
            "Product Reviews Written",
            min_value=0,
            value=3
        )

        Social_Media_Engagement_Score = st.number_input(
            "Social Media Engagement Score",
            min_value=0,
            value=70
        )

        Mobile_App_Usage = st.selectbox(
            "Mobile App Usage",
            [0, 1]
        )

        Payment_Method_Diversity = st.number_input(
            "Payment Method Diversity",
            min_value=0,
            value=2
        )

        Credit_Balance = st.number_input(
            "Credit Balance",
            min_value=0.0,
            value=1000.0
        )

        Country = st.selectbox(
            "Country",
            [
                "India",
                "USA",
                "UK",
                "Canada",
                "Germany"
            ]
        )

        Signup_Quarter = st.selectbox(
            "Signup Quarter",
            [
                "Q1",
                "Q2",
                "Q3",
                "Q4"
            ]
        )

    # ==========================================
    # CREATE INPUT DATAFRAME
    # ==========================================

    input_data = pd.DataFrame({
        'Age': [Age],
        'Gender': [Gender],
        'Membership_Years': [Membership_Years],
        'Login_Frequency': [Login_Frequency],
        'Session_Duration_Avg': [Session_Duration_Avg],
        'Pages_Per_Session': [Pages_Per_Session],
        'Cart_Abandonment_Rate': [Cart_Abandonment_Rate],
        'Wishlist_Items': [Wishlist_Items],
        'Total_Purchases': [Total_Purchases],
        'Average_Order_Value': [Average_Order_Value],
        'Lifetime_Value': [Lifetime_Value],
        'Days_Since_Last_Purchase': [Days_Since_Last_Purchase],
        'Discount_Usage_Rate': [Discount_Usage_Rate],
        'Returns_Rate': [Returns_Rate],
        'Email_Open_Rate': [Email_Open_Rate],
        'Customer_Service_Calls': [Customer_Service_Calls],
        'Product_Reviews_Written': [Product_Reviews_Written],
        'Social_Media_Engagement_Score': [Social_Media_Engagement_Score],
        'Mobile_App_Usage': [Mobile_App_Usage],
        'Payment_Method_Diversity': [Payment_Method_Diversity],
        'Credit_Balance': [Credit_Balance],
        'Country': [Country],
        'Signup_Quarter': [Signup_Quarter]
    })

    # ==========================================
    # PREDICT BUTTON
    # ==========================================

    if st.button("Predict Churn"):

        try:

            if hasattr(pipeline, "feature_names_in_"):

                expected_features = pipeline.feature_names_in_

                missing_from_df = set(expected_features) - set(input_data.columns)

                if missing_from_df:

                    st.error(
                        f"UI Error: Missing Features: {missing_from_df}"
                    )

                    st.stop()

                input_data = input_data[expected_features]

            # ==========================
            # MAKE PREDICTION
            # ==========================

            prediction = pipeline.predict(input_data)

            probability = pipeline.predict_proba(input_data)

            churn_probability = probability[0][1] * 100

            # ==========================
            # STORE PREDICTION RESULTS
            # ==========================

            prediction_value = int(prediction[0])

            result_data = input_data.copy()

            result_data["Prediction"] = prediction_value

            result_data["Prediction_Label"] = (
                "Customer Likely To Churn"
                if prediction_value == 1
                else "Customer Will Stay"
            )

            result_data["Churn_Probability"] = round(
                churn_probability,
                2
            )

            result_data["Prediction_Time"] = pd.Timestamp.now()

            csv_file = "customer_predictions.csv"

            # ==========================
            # APPEND CSV
            # ==========================

            if os.path.exists(csv_file):

                existing_data = pd.read_csv(csv_file)

                updated_data = pd.concat(
                    [existing_data, result_data],
                    ignore_index=True
                )

            else:

                updated_data = result_data

            # ==========================
            # SAVE CSV
            # ==========================

            updated_data.to_csv(
                csv_file,
                index=False
            )

            # ==========================
            # SHOW PROBABILITY
            # ==========================

            st.subheader("Churn Probability")

            st.progress(
                int(churn_probability)
            )

            st.write(
                f"Churn Probability: {churn_probability:.2f}%"
            )

            # ==========================
            # RISK LEVEL
            # ==========================

            st.subheader("Risk Level")

            if churn_probability >= 80:

                st.error(
                    "Very High Risk Customer"
                )

            elif churn_probability >= 60:

                st.warning(
                    "High Risk Customer"
                )

            elif churn_probability >= 40:

                st.warning(
                    "Medium Risk Customer"
                )

            else:

                st.success(
                    "Low Risk Customer"
                )

            # ==========================
            # AI BUSINESS INSIGHTS
            # ==========================

            st.subheader("AI Business Insights")

            insights = []

            if Cart_Abandonment_Rate > 0.5:

                insights.append(
                    "High cart abandonment detected."
                )

            if Login_Frequency < 5:

                insights.append(
                    "Low login frequency indicates low engagement."
                )

            if Days_Since_Last_Purchase > 30:

                insights.append(
                    "Customer inactive for long duration."
                )

            if Returns_Rate > 0.4:

                insights.append(
                    "High returns rate increases churn risk."
                )

            if Discount_Usage_Rate > 0.7:

                insights.append(
                    "Customer heavily dependent on discounts."
                )

            if len(insights) == 0:

                st.success(
                    "Customer behavior appears healthy."
                )

            else:

                for insight in insights:

                    st.warning(insight)

            # ==========================
            # RETENTION SUGGESTIONS
            # ==========================

            st.subheader("Retention Suggestions")

            if churn_probability > 70:

                st.write("""
                ✅ Offer discount coupons  
                ✅ Send personalized offers  
                ✅ Improve customer engagement  
                ✅ Provide loyalty rewards  
                """)

            elif churn_probability > 40:

                st.write("""
                ✅ Send reminder emails  
                ✅ Increase product recommendations  
                ✅ Offer membership benefits  
                """)

            else:

                st.write("""
                ✅ Customer retention looks stable  
                """)

        except Exception as e:

            st.error(f"Prediction Error: {e}")

# ==========================================
# FOOTER
# ==========================================

st.write("---")

st.write(
    "Developed Using Streamlit + Machine Learning"
) 