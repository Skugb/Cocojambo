# models.py
class Vacancy(BaseModel):
    id = UUID
    external_id = String  # ID из внешнего API
    source = String  # 'hh', 'habr', etc
    title = String
    description = Text
    url = String
    is_actual = Boolean
    published_at = DateTime
    created_at = DateTime
    updated_at = DateTime

class Technology(BaseModel):
    id = UUID
    name = String  # нормализованное название
    created_at = DateTime

class VacancyTechnology(BaseModel):
    id = UUID
    vacancy_id = ForeignKey
    technology_id = ForeignKey
    found_at = DateTime
    search_type = String  # 'exact', 'partial'

class SearchCache(BaseModel):
    id = UUID
    vacancy_id = ForeignKey
    technology_id = ForeignKey
    has_technology = Boolean
    checked_at = DateTime
    is_actual = Boolean

class StatisticsDaily(BaseModel):
    id = UUID
    vacancy_query = String
    technology_name = String
    total_vacancies = Integer
    vacancies_with_technology = Integer
    percentage = Float
    calculation_date = Date