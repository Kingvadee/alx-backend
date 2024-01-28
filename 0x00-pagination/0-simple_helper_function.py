from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    # Ensure page and page_size are greater than 0
    assert page > 0 and page_size > 0, "Page and page_size must be greater than 0"
    
    # Calculate start index
    start_index = (page - 1) * page_size
    
    # Calculate end index
    end_index = start_index + page_size
    
    return start_index, end_index

