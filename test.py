# 账户终值计算（复利+每月缴费）
def account_future(principal, monthly_in, years, annual_rate=0.03):
    n = int(years * 12)
    r = annual_rate / 12
    # 本金复利
    fv_principal = principal * (1 + r) ** n
    # 每月缴费年金终值
    fv_payment = monthly_in * (((1 + r) ** n - 1) / r)
    return round(fv_principal + fv_payment, 2)


# 输出结果
print("女教师退休账户（保守3%收益率）")
print(f"养老个人账户：{female_pension} 元")
print(f"职业年金账户：{female_annuity} 元\n")

print("男教师退休账户（保守3%收益率）")
print(f"养老个人账户：{male_pension} 元")
print(f"职业年金账户：{male_annuity} 元")