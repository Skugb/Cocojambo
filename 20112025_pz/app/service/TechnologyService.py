class TechnologyService:
    async def normalize_technology_name(self, name: str) -> str
    async def validate_technology(self, name: str) -> bool
    async def find_similar_technologies(self, name: str) -> List[Technology]