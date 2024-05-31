from handlers.base_handler import BaseHandler

class DeliveryCountryHandler(BaseHandler):
    def __init__(self, supported_countries=None):
        super().__init__()
        self.supported_countries = supported_countries

    def handle(self, request):
        result = self.check_country_is_in_supported_list(request)
        if result:
            return result
        return super().handle(request)
    
    def check_country_is_in_supported_list(self, request):
        delivery_country = request.delivery_details['country']
        if delivery_country not in self.supported_countries:
            return self.fail_response(f"Country {delivery_country} is not supported for delivery")
        return None