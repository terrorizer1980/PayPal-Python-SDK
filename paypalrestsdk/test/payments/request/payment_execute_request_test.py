# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# payment_execute_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"payment.execute","Description":"Executes a PayPal payment that the customer has approved. You can optionally update one or more transactions when you execute the payment.\u003cblockquote\u003e\u003cstrong\u003eImportant:\u003c/strong\u003e This call works only after a customer has approved the payment. For more information, learn about [PayPal payments](/docs/integration/direct/payments/paypal-payments/).\u003c/blockquote\u003e","Parameters":[{"Type":"string","VariableName":"payment_id","Description":"The ID of the payment to execute.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Payment Execution","VariableName":"body","Description":"Executes a PayPal account-based payment with the `payer_id` obtained from the web approval URL.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Payment","VariableName":"","Description":"A payment. Use this object to create, process, and manage payments.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/payment/{payment_id}/execute","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.payments.request import PaymentExecuteRequest
from paypalrestsdk.test.testharness import TestHarness
from payment_create_request_test import createPayment

class PaymentExecuteRequestTest(TestHarness):

    def testPaymentExecuteRequestTest(self):
        self.skipTest("Tests that use this class must be ignored when run in an automated environment because executing an order will require approval via the executed payment's approval_url")

        response = createPayment(self.client, "order")

        request = PaymentExecuteRequest(response.result.id)
        request.body({
            "payer_id": "some_payer_id"
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
