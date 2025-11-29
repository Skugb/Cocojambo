class VacancyService:
    async def search_vacancies(self, query: str, exact_match: bool) -> List[Vacancy]
    async def update_vacancies_cache(self)
    async def get_vacancy_technologies(self, vacancy_id: UUID) -> List[Technology]