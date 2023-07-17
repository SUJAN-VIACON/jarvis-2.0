class GlobalVariable:
    global_text = "..."  # Define the global variable at the class level

    @staticmethod
    def getValue():
        return GlobalVariable.global_text

    @staticmethod
    def setValue(value):
        GlobalVariable.global_text = value