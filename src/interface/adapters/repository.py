from abc import ABC, abstractmethod
from typing import List

from interface.domain.inputs import Product, QualityAssurance


class ProductRepository(ABC):
    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass


class QualityAssuranceRepository(ABC):
    @abstractmethod
    def add_inspection(self, inspection: QualityAssurance) -> None:
        pass

    @abstractmethod
    def get_inspections(self) -> List[QualityAssurance]:
        pass

    @abstractmethod
    def get_inspections_for_product(self, product_id: int) -> List[QualityAssurance]:
        pass

    @abstractmethod
    def update_inspections_for_product(self, product_id: int) -> List[QualityAssurance]:
        pass
