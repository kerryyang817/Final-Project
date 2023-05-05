from typing import List
from interface.adapters.repository import ProductRepository
from interface.domain.inputs import QualityAssurance


class QualityAssuranceService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def get_quality_assurance_data(self, start_date: str, end_date: str) -> List[QualityAssurance]:
        data = self.repo.get_quality_assurance_data(start_date, end_date)
        return data

    def add_quality_assurance_data(self, data: QualityAssurance):
        self.repo.add_quality_assurance_data(data)

    def update_quality_assurance_data(self, id: int, data: QualityAssurance):
        self.repo.update_quality_assurance_data(id, data)

    def delete_quality_assurance_data(self, id: int):
        self.repo.delete_quality_assurance_data(id)
