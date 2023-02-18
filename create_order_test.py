import steps

# Тест 1. По треку заказа можно получить данные о заказе
def test_get_order_by_track():
    current_order = steps.response_get_order_by_track
    assert current_order.status_code == 200



