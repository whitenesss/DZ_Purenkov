import pytest
from develop.class_category import Category


@pytest.fixture
def test_catgory():
    return Category('name', 'description', ["55\" QLED 4K", "Фоновая подсветка", 123000.0, 7])


def test_init_category(test_catgory):
    assert test_catgory.request_name() == 'name'
    assert test_catgory.description == 'description'
    assert test_catgory.request_products() == ["55\" QLED 4K", "Фоновая подсветка", 123000.0, 7]


def test_f_category(test_catgory):
    assert test_catgory.request_description_1 == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'
    assert test_catgory.unique_products == 8
    assert test_catgory.total_numbers_of_category == 2