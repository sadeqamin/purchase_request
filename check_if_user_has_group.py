@api.model
def _default_x_is_admin(self):
     return self.env.user.has_group('purchase_request.group_purchase_request_can_reset')
