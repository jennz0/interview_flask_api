from database import db, Todo

class TodoService:
    def get_todo_list(self):
        return db.query(Todo).all()
    
    def get_todo(self, todo_id):
        return db.query(Todo).filter(Todo.todoId == todo_id)
    
    def create_todo(self, todo_item):
        try:
            todo_object = Todo(**todo_item)
            db.add(todo_object)
            db.commit()
            return True, "todo item created"
        except Exception:
            db.rollback()
            return False, str(Exception)
    
    def update_todo(self, todo_id, todo_item):
        item_to_update = db.query(Todo).filter(Todo.todoId == todo_id)
        if item_to_update:
            if "status" in todo_item:
                item_to_update.status = todo_item["status"]
            if "description" in todo_item:
                item_to_update.description = todo_item["description"]
            db.commit()
            return True, "update successful"
        return False, "update item not found"
        
        

    def delete_todo(self, todo_id):
        db.query(Todo).filter(Todo.todoId == todo_id).delete()
        db.commit()

    
