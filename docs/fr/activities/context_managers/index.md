# Les context managers

## Exercices

 * [Premier exercice](activity_1.md)
 * [Second exercice](activity_2.md)
 * [Troisième exercice](activity_3.md)

## Rappels
```python
class MyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass
```