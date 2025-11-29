class StatisticsService:
    async def calculate_percentage(self, vacancy_query: str, technology: str, 
                                 exact_match: bool) -> StatisticsResult
    async def get_historical_data(self, vacancy_query: str, technology: str,
                                days: int) -> List[DailyStatistics]