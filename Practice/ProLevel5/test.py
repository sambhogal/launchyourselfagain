






str = """class ModelDatabase(models.Model):

    label = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=100,blank=True)

    def get_absolute_url(self):
        return reverse('base_app:create_modeldb_fields_url')

    def __str__(self):
        return self.name"""

str2 = """class loki():
            def nam(self):
                return 'loki'"""

exec(str2)
a = loki()
print(a.nam())                















# # class Robot:
# #     counter = 0
# #     def __init__(self, name):
# #         self.name = name
# #     def sayHello(self):
# #         return "Hi, I am " + self.name
#
#
# def Rob_init(self, name):
#     self.name = name
#
# Robot2 = type("Robot2",
#               (),
#               {"counter":0,
#                "__init__": Rob_init,
#                "sayHello": lambda self: "Hi, I am " + self.name,
#                "fun1": lambda self: 'Loki'},
#                )
#
# print(Robot2)
# x = Robot2("Marvin")
# print(x.fun1())
# # print(x.sayHello())
# # y = Robot("Marvin")
# # print(y.name)
# # print(y.sayHello())
# # print(x.__dict__)
# # print(y.__dict__)
#
#
# exec("""def a(x):
#         return x+1""")
# a(2)
