class Loan:
    _loans = []
    loan_id = 1

    @classmethod
    def create_loan(cls, amount, term, user_id):
        loan = {
            'id': cls.loan_id,
            'amount': amount,
            'term': term,
            'status': 'PENDING',
            'repayments': cls._generate_repayments(amount, term),
            'user_id': int(user_id)

        }
        cls.loan_id += 1
        cls._loans.append(loan)
        return loan

    @classmethod
    def get_loans(cls, user_id):
        print("get_loans called for ",user_id)
        print("current loans ", cls._loans)
        if user_id:
            return [loan for loan in cls._loans if loan['user_id'] == int(user_id)]
        return cls._loans

    @staticmethod
    def _generate_repayments(amount, term):
        weekly_amount = round(amount / term, 2)
        last_payment = amount - (weekly_amount * (term - 1))
        repayments = []
        for i in range(term):
            amount = last_payment if i == term - 1 else weekly_amount
            repayments.append({'amount': amount, 'status': 'PENDING'})
        return repayments

    @classmethod
    def add_repayment(cls, loan_id, repayment_id, amount, user_id):
        for loan in cls._loans:
            if loan['id'] == loan_id and loan['user_id'] == user_id:
                if amount >= loan['repayments'][repayment_id]['amount']:
                    loan['repayments'][repayment_id]['status'] = 'PAID'
                    if all(repayment['status'] == 'PAID' for repayment in loan['repayments']):
                        loan['status'] = 'PAID'
                    return True, "Repayment added successfully!"
                else:
                    return False, "Repayment amount must be greater than or equal to the scheduled repayment."
        return False, "Loan not found or does not belong to the user."
