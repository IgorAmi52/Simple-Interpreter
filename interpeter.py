class Interpreter:
    def __init__(self):
        self.var = []  # List of variable names
        self.val = []  # List of variable values
        self.scope_indexes = [0]  # Stack to track scope boundaries
    
    def interpret(self, raw_code):
        lines = raw_code.split('\n')
        for line in lines:
            tokens = line.split(' ')
            tokens = [token for token in tokens if token]  # Remove empty strings
            if tokens[0] == 'scope':
                # Start a new scope
                self.scope_indexes.append(len(self.var))
                continue
            
            if tokens[0] == '}':
                # End the current scope
                end_scope = self.scope_indexes.pop()
                self.var = self.var[:end_scope]
                self.val = self.val[:end_scope]
                continue
            
            if tokens[0] == 'print':
                # Print the value of a variable
                value, _ = self.find_val(tokens[1])
                print(value if value is not None else 'null')
                continue
            
            if tokens[2].isdigit():
                # Assign a numeric value to a variable
                # if value is already assigned, update it
                self.update_value(tokens[0], int(tokens[2]), self.scope_indexes[-1])
            else:
                # Assign the value of another variable
                value, _ = self.find_val(tokens[2])
                if value is not None:
                    self.update_value(tokens[0], value, self.scope_indexes[-1])

        self.scope_indexes = [0]
        self.val = []
        self.var = []
    
    def find_val(self, var_name, scope=0):
        # Find the value of a variable in reverse order
        for i in range(len(self.var) - 1, -1 + scope, -1):
            if self.var[i] == var_name:
                return self.val[i], i
        return None, None
    
    def update_value(self, var_name, value, scope):
        # Update the value of a variable if it exists in the scope, or create a new variable
        _, index = self.find_val(var_name, scope)
        if index is not None:
            self.val[index] = value
        else:
            self.var.append(var_name)
            self.val.append(value)
