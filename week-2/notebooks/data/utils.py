# utils.py — вспомогательные функции

def normalize(nums):
    """Привести список чисел в диапазон 0..1"""
    min_val = min(nums)
    max_val = max(nums)
    
    if min_val == max_val:
        return [0] * len(nums)
    
    return [(x - min_val) / (max_val - min_val) for x in nums]


def top_k(scores: dict, k: int):
    """Вернуть топ-k элементов словаря по убыванию значения"""
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:k]


def safe_div(a, b):
    """Безопасное деление — возвращает None если b=0"""
    if b == 0:
        return None
    return a / b

def count_words(filepath: str):
    """Посчитать статистику по файлу"""
    from collections import Counter
    from pathlib import Path
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    words = content.split()
    lines = content.strip().split("\n")
    
    return {
        "lines": len(lines),
        "words": len(words),
        "unique": len(set(words)),
        "top_10": Counter(words).most_common(10)
}