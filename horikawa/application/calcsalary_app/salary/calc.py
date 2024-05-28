# 給与計算用

# 給与額の入力を受け付け、"支給額"と"税額"を返す
# 100万以下は税率10%, 100万以上は超えた部分が税率20%
# 税率の変わる給与額を変数で管理して、税率を計算
def calc_salary(salary):
    
    # 税率の変わる給与額を管理する変数
    taxChange_amount = 1000000

    # 税額
    tax_answer = 0

    salary = int(salary)
    if salary >= taxChange_amount:
        tax_answer = taxChange_amount * 0.1 + (salary - taxChange_amount) * 0.2
    else:
        tax_answer = salary * 0.1

    # 税額の四捨五入
    tax_answer = round(tax_answer)

    # 支給額(給与額 - 税額)
    salary_answer = salary - tax_answer

    # 実行
    return "給与：{0}円の場合、支給額:{1}、税額:{2}です。".format(salary,salary_answer,tax_answer)
