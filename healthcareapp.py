import streamlit as st

# Blood Testing
class BloodTestings:
    def sugar_testing(self, glucose):
        if glucose < 70:
            return 'Low Blood Sugar Level'
        elif glucose > 100:
            return 'High Blood Sugar Level'
        else:
            return 'Average Blood Sugar Level'

    def blood_testing(self, blood):
        if blood < 4.2:
            return 'Low Hemoglobin'
        elif blood > 5.7:
            return 'High Hemoglobin'
        else:
            return 'Average Hemoglobin'


# Vitamin Testing
class VitaminTesting:
    def vitamin_B12(self, vitaminb12):
        if vitaminb12 < 197:
            return 'Insufficient Count of Vitamin B12'
        elif vitaminb12 > 771:
            return 'Upper Count of Vitamin B12 from Safety Limit'
        else:
            return 'Sufficient Count of Vitamin B12'

    def vitamin_D(self, vitaminD):
        if vitaminD < 30:
            return 'Insufficient Count of Vitamin D'
        elif vitaminD > 100:
            return 'Upper Count of Vitamin D from Safety Limit'
        else:
            return 'Sufficient Count of Vitamin D'


# Thyroid Testing
class ThyroidTesting:
    def t3_testing(self, t3):
        if t3 < 0.8:
            return 'Insufficient Count of Tri-Iodothyronine (T3)'
        elif t3 > 2.0:
            return 'Upper Count of Tri-Iodothyronine (T3)'
        else:
            return 'Sufficient Count of Tri-Iodothyronine (T3)'

    def t4_testing(self, t4):
        if t4 < 5.1:
            return 'Insufficient Count of Thyroxine/T4'
        elif t4 > 14.1:
            return 'Upper Count of Thyroxine/T4'
        else:
            return 'Sufficient Count of Thyroxine/T4'

    def tsh_testing(self, tsh):
        if tsh < 5.1:
            return 'Insufficient Count of Thyroid Stimulating Hormone/TSH'
        elif tsh > 14.1:
            return 'Upper Count of Thyroid Stimulating Hormone/TSH'
        else:
            return 'Sufficient Count of Thyroid Stimulating Hormone/TSH'


# Chemical Exam
class ChemicalExam:
    def specific_gravity(self, gravity):
        if gravity < 1.001:
            return 'Good'
        elif gravity > 1.035:
            return 'Bad'
        else:
            return 'Average'

    def ph_testing(self, ph):
        if ph < 4.5:
            return 'Acidic'
        elif ph > 7.5:
            return 'Alkaline'
        else:
            return 'Neutral'


# Lipid Profile
class LipidProfile:
    def total_cholestrol(self, tc):
        if tc < 200:
            return 'Desirable Total Cholesterol'
        elif tc >= 240:
            return 'High Total Cholesterol'
        else:
            return 'Borderline Total Cholesterol'

    def HDL_Cholestrol(self, HDL):
        if HDL < 40:
            return 'Low Serum HDL Cholesterol'
        elif HDL > 60:
            return 'High Serum HDL Cholesterol'
        else:
            return 'Average Serum HDL Cholesterol'

    def LDL_Cholestrol(self, LDL):
        if LDL < 100:
            return 'Optimal Serum LDL Cholesterol'
        elif LDL > 160:
            return 'High Serum LDL Cholesterol'
        else:
            return 'Borderline Serum LDL Cholesterol'

    def NHDL_Cholestrol(self, NHDL):
        if NHDL < 0:
             return 'Low Non-HDL Cholestrol'
        elif NHDL > 160 :
            return 'High Non-HDL Cholestrol'
        else:
            return 'Average Non-HDL Cholestrol'


# Liver Function Test (LFT)
class LFT:
    def Serum_Bilirubin(self, sb):
        if sb < 0:
            return 'Low Serum Bilirubin'
        elif sb >= 1.2:
            return 'High Serum Bilirubin'
        else:
            return 'Average Serum Bilirubin'
    def ALP(self, alp):
        if alp < 40 :
            return 'Low Alkaline Phosphate'
        elif alp > 129:
            return 'High Alkaline Phosphate'
        else:
            return 'Average Alkaline Phosphate'
    def GGT (self, ggt):

        if ggt < 10 :
            return 'Low Gamma Glutamyl Transferase'
        elif ggt > 71 :
            return 'High Gamma Glutamyl Transferase'
        else:
            return 'Average Gamma Glutamyl Transferase'
    def STP(self, stp):
        if stp < 6.4 :
            return 'Low Serum Total Protien'
        elif stp > 8.3 :
            return 'High Serum Total Protien'
        else:
            return 'Average Serum Total Protien'
    def SA(self, sa):
        if sa < 6.4 :
            return 'Low Serum Albumin'
        elif sa > 8.3 :
            return 'High Serum Albumin'
        else:
            return 'Average Serum Albumin'

    def SG(self, sg):
        if sg < 2.0 :
            return 'Low Serum Globulin'
        elif sg > 3.5 :
            return 'High Serum Globulin'
        else:
            return 'Average Serum Globulin'

# Kidney Function Test (KFT)
class KFT:
    def Serum_Creatinine(self, sc):
        if sc < 0.70:
            return 'Low Serum Creatinine'
        elif sc > 1.20:
            return 'High Serum Creatinine'
        else:
            return 'Average Serum Creatinine'

    def SCAL(self, scal):
        if scal < 8.6:
            return 'Low Serum Calcium'
        elif scal > 10.0:
            return 'High Serum Calcium'
        else:
            return 'Average Serum Calcium'

    def SPHOS(self, sphos):
        if sphos < 2.5 :
            return 'Low Serum Phosphorus'
        elif sphos > 4.5 :
            return 'High Serum Phosphorus'
        else:
            return 'Average Serum Phosphorus'

    def SSOD(self, ssod):

        if ssod < 136 :
            return 'Low Serum Sodium'
        elif ssod > 145 :
            return 'High Serum Sodium'
        else:
            return 'Average Serum Sodium'

    def SPOT(self, spot):

        if spot < 3.5 :
            return 'Low Serum Pottasium '
        elif spot > 5.1 :
            return 'High Serum Pottasium '
        else:
            return 'Average Serum Pottasium '

    def SCHL(self, schl):

        if schl < 98 :
            return 'Low Serum Chloride'
        elif schl > 107 :
            return 'High Serum Chloride'
        else:
            return 'Average Serum Chloride'

    def BUREA(self, burea):
        if burea < 16.6 :
            return 'Low Blood Urea'
        elif burea > 48.5 :
            return 'High Blood Urea'
        else:
            return 'Average Blood Urea'


# Streamlit UI
def main():
    st.title("Health Checkup API")
    st.sidebar.header("Select Test Category")

    categories = ['Blood Testing', 'Vitamin Testing', 'Thyroid Testing', 'Chemical Exam', 'Lipid Profile', 'LFT', 'KFT']
    choice = st.sidebar.selectbox("Choose a Test", categories)

    # Blood Testing
    if choice == 'Blood Testing':
        st.subheader("Blood Testing")
        glucose = st.number_input("Enter Glucose (Fasting, mg/dl)", min_value=0)
        blood = st.number_input("Enter Hemoglobin (g/dL)", min_value=0)

        if st.button("Get Results"):
            blood_test = BloodTestings()
            st.write(blood_test.sugar_testing(glucose))
            st.write(blood_test.blood_testing(blood))

    # Vitamin Testing
    elif choice == 'Vitamin Testing':
        st.subheader("Vitamin Testing")
        vitamin_b12 = st.number_input("Enter Vitamin B12 (pg/ml)", min_value=0)
        vitamin_d = st.number_input("Enter Vitamin D (ng/ml)", min_value=0)

        if st.button("Get Results"):
            vitamin_test = VitaminTesting()
            st.write(vitamin_test.vitamin_B12(vitamin_b12))
            st.write(vitamin_test.vitamin_D(vitamin_d))

    # Thyroid Testing
    elif choice == 'Thyroid Testing':
        st.subheader("Thyroid Testing")
        t3 = st.number_input("Enter Tri-Iodothyronine (T3) (ng/ml)", min_value=0.0)
        t4 = st.number_input("Enter Thyroxine (T4) (µg/dL)", min_value=0.0)
        tsh = st.number_input("Enter Thyroid Stimulating Hormone (TSH) (µIU/mL)", min_value=0.0)

        if st.button("Get Results"):
            thyroid_test = ThyroidTesting()
            st.write(thyroid_test.t3_testing(t3))
            st.write(thyroid_test.t4_testing(t4))
            st.write(thyroid_test.tsh_testing(tsh))

    # Chemical Exam
    elif choice == 'Chemical Exam':
        st.subheader("Chemical Exam")
        gravity = st.number_input("Enter Specific Gravity", min_value=1.000)
        ph = st.number_input("Enter pH Value", min_value=0.0)

        if st.button("Get Results"):
            chemical_exam = ChemicalExam()
            st.write(chemical_exam.specific_gravity(gravity))
            st.write(chemical_exam.ph_testing(ph))

    # Lipid Profile
    elif choice == 'Lipid Profile':
        st.subheader("Lipid Profile")
        tc = st.number_input("Enter Total Cholesterol (mg/dL)", min_value=0)
        hdl = st.number_input("Enter HDL Cholesterol (mg/dL)", min_value=0)
        ldl = st.number_input("Enter LDL Cholesterol (mg/dL)", min_value=0)
        nhdl = st.number_input("Enter NHDL Cholesterol (mg/dL)", min_value=0)

        if st.button("Get Results"):
            lipid_profile = LipidProfile()
            st.write(lipid_profile.total_cholestrol(tc))
            st.write(lipid_profile.HDL_Cholestrol(hdl))
            st.write(lipid_profile.LDL_Cholestrol(ldl))
            st.write(lipid_profile.NHDL_Cholestrol(nhdl))

    # Liver Function Test (LFT)
    elif choice == 'LFT':
        st.subheader("Liver Function Test (LFT)")
        sb = st.number_input("Enter Serum Bilirubin (mg/dL)", min_value=0.0)
        alp = st.number_input("Enter Alkaline Phosphate (mg/dL)", min_value=0.0)
        ggt = st.number_input("Enter Gamma Glutamyl Transferase (mg/dL)", min_value=0.0)
        stp = st.number_input("Enter Serum Total Protien (mg/dL)", min_value=0.0)
        sa = st.number_input("Enter Serum Albumin (mg/dL)", min_value=0.0)
        sg = st.number_input("Enter Serum Globulin (mg/dL)", min_value=0.0)

        if st.button("Get Results"):
            lft = LFT()
            st.write(lft.Serum_Bilirubin(sb))
            st.write(lft.ALP(alp))
            st.write(lft.GGT(ggt))
            st.write(lft.STP(stp))
            st.write(lft.SA(sa))
            st.write(lft.SG(sg))

    # Kidney Function Test (KFT)
    elif choice == 'KFT':
        st.subheader("Kidney Function Test (KFT)")
        sc = st.number_input("Enter Serum Creatinine (mg/dL)", min_value=0.0)
        scal = st.number_input("Enter Serum Calcium (mg/dL)", min_value=0.0)
        sphos = st.number_input("Enter Serum Phosphorus (mg/dL)", min_value=0.0)
        ssod = st.number_input("Enter Serum Sodium (mg/dL)", min_value=0.0)
        spot = st.number_input("Enter Serum Pottasium (mg/dL)", min_value=0.0)
        schl = st.number_input("Enter Serum Chloride (mg/dL)", min_value=0.0)
        burea = st.number_input("Enter Blood Urea (mg/dL)", min_value=0.0)

        if st.button("Get Results"):
            kft = KFT()
            st.write(kft.Serum_Creatinine(sc))
            st.write(kft.SCAL(scal))
            st.write(kft.SPHOS(sphos))
            st.write(kft.SSOD(ssod))
            st.write(kft.SPOT(spot))
            st.write(kft.SCHL(schl))
            st.write(kft.BUREA(burea))


if __name__ == "__main__":
    main()
