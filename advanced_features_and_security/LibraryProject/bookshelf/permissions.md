## Permissions and Groups Setup

### Permissions

The following permissions are defined in the `Book` model:

- `can_view`: View books.
- `can_create`: Add new books.
- `can_edit`: Modify book details.
- `can_delete`: Remove books.

### Groups

Three user groups are configured:

1. **Viewers**: `can_view`
2. **Editors**: `can_view`, `can_create`, `can_edit`
3. **Admins**: All permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

### Enforcing Permissions

Views are protected using Django's `@permission_required` decorator. For example:

```python
@permission_required('your_app.can_edit', raise_exception=True)
```
