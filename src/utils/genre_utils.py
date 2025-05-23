"""
Utility functions for genre-specific operations.

This module provides utility functions for determining genre-specific behavior
and characteristics.
"""



def should_generate_characters(genre: str) -> bool:
    """
    Determine if character generation is needed for a given genre.

    Args:
        genre: The genre of the book

    Returns:
        bool: True if characters should be generated, False otherwise
    """
    # Fiction genres that need characters (narrative content)
    fiction_genres = [
        "literary fiction", "commercial fiction", "mystery", "mystery thriller",
        "thriller", "romance", "fantasy", "epic fantasy", "science fiction",
        "historical fiction", "horror", "young adult", "middle grade",
        "children's chapter books", "speculative fiction", "alternate history",
        "contemporary fiction", "paranormal romance", "urban fantasy", "dystopian",
        "test"  # Include test genre for development
    ]

    # Special formats that might need characters
    special_fiction_formats = [
        "short story collection", "novella", "graphic novel"
    ]

    # Non-fiction genres that don't need characters
    non_fiction_genres = [
        "memoir", "biography", "history", "self-help", "business",
        "popular science", "academic", "travel", "cookbook", "how-to",
        "essay collection", "philosophy", "true crime", "poetry collection",
        "creative non-fiction"
    ]

    # Check if it's a fiction genre that needs characters
    genre_lower = genre.lower()

    # Check fiction genres first
    for fiction_genre in fiction_genres:
        if fiction_genre in genre_lower:
            return True

    # Check special fiction formats
    for special_format in special_fiction_formats:
        if special_format in genre_lower:
            return True

    # Check if it's explicitly non-fiction
    for non_fiction_genre in non_fiction_genres:
        if non_fiction_genre in genre_lower:
            return False

    # Default to True for unknown genres (assume fiction)
    return True


def is_special_format(genre: str) -> bool:
    """
    Determine if a genre is a special format that uses sections instead of chapters.

    Args:
        genre: The genre of the book

    Returns:
        bool: True if it's a special format, False otherwise
    """
    special_formats = [
        "poetry collection", "graphic novel", "essay collection",
        "short story collection", "cookbook", "travel guide", "travel"
    ]

    genre_lower = genre.lower()
    return any(special_format in genre_lower for special_format in special_formats)


def get_genre_format_type(genre: str) -> str:
    """
    Determine the format type for EPUB generation.

    Args:
        genre: The genre of the book

    Returns:
        str: Format type for specialized EPUB handling
    """
    genre_lower = genre.lower()

    # Poetry collections need special line break handling
    if "poetry" in genre_lower:
        return "poetry"

    # Cookbooks need recipe formatting
    if "cookbook" in genre_lower:
        return "cookbook"

    # Travel guides need location-based formatting
    if "travel" in genre_lower:
        return "travel"

    # Graphic novels need visual formatting
    if "graphic novel" in genre_lower:
        return "graphic_novel"

    # Essay collections need essay formatting
    if "essay" in genre_lower:
        return "essay"

    # Short story collections need story separation
    if "short story" in genre_lower:
        return "short_story"

    # Self-help books need structured formatting
    if "self-help" in genre_lower or "self help" in genre_lower:
        return "self_help"

    # Biography/memoir need chronological formatting
    if "biography" in genre_lower or "memoir" in genre_lower:
        return "biography"

    # Business books need professional formatting
    if "business" in genre_lower:
        return "business"

    # Academic/educational books need structured formatting
    if any(term in genre_lower for term in ["academic", "history", "philosophy", "popular science"]):
        return "academic"

    # Default to standard formatting
    return "standard"


def get_content_terminology(genre: str) -> str:
    """
    Get the appropriate terminology for content divisions (chapters vs sections).

    Args:
        genre: The genre of the book

    Returns:
        str: "chapters" or "sections"
    """
    if is_special_format(genre):
        if "poetry" in genre.lower():
            return "sections"
        elif "collection" in genre.lower():
            return "pieces"
        else:
            return "sections"
    else:
        return "chapters"


def is_fiction_genre(genre: str) -> bool:
    """
    Determine if a genre is fiction or non-fiction.

    Args:
        genre: The genre of the book

    Returns:
        bool: True if fiction, False if non-fiction
    """
    fiction_genres = [
        "literary fiction", "commercial fiction", "mystery", "mystery thriller",
        "thriller", "romance", "fantasy", "epic fantasy", "science fiction",
        "historical fiction", "horror", "young adult", "middle grade",
        "children's chapter books", "speculative fiction", "alternate history",
        "contemporary fiction", "paranormal romance", "urban fantasy", "dystopian",
        "short story collection", "novella", "graphic novel", "test"
    ]

    genre_lower = genre.lower()
    return any(fiction_genre in genre_lower for fiction_genre in fiction_genres)
