import pandas as pd
import os

def load_data():
    """M&E Device data တွေကို ဒီမှာ ထည့်သွင်းသတ်မှတ်ပေးပါတယ်"""
    data = {
        'Device': ['Generator', 'Chiller 1', 'Chiller 2', 'UPS', 'AC Unit'],
        'Status': ['Running', 'Running', 'Down', 'Running', 'Down'],
        'Temperature': [65, 70, 0, 45, 80]
    }
    return pd.DataFrame(data)

def check_warnings(df):
    """အပူချိန် 75 ကျော်ရင် Warning ပေးမယ့် function"""
    def temp_status(temp):
        return "WARNING" if temp > 75 else "Normal"
    
    df['Temp_Alert'] = df['Temperature'].apply(temp_status)
    return df

def main():
    print("--- M&E Automation System စတင်ပါပြီ ---")
    
    # ၁။ Data ရယူခြင်း
    df = load_data()
    
    # ၂။ Warning စစ်ဆေးခြင်း
    df = check_warnings(df)
    print("\n[Current Device Status]")
    print(df)
    
    # ၃။ 'Down' ဖြစ်နေတဲ့ Device တွေကို စစ်ထုတ်ခြင်း
    faulty_devices = df[df['Status'] == 'Down']
    
    print("\n[Faulty Devices Found]")
    print(faulty_devices)
    
    # ၄။ Excel ဖိုင်အဖြစ် သိမ်းဆည်းခြင်း
    output_file = 'me_report.xlsx'
    df.to_excel(output_file, index=False)
    print(f"\nReport အား '{output_file}' အဖြစ် အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ။")

if __name__ == "__main__":
    main()

