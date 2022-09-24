# exec(open(r"D:\python_learning\Python_Practice\django\Hospital\db_shell.py").read())



from HSPTL.models import Department, Doctor, Hospital, Owner

# # a = Doctor.objects.get()


# d = [Hospital(Name='Sr.J.J.Hospital',Phone_num=123456,esta_year='1995-3-23'),
# Hospital(Name='Sion Hospital',Phone_num=123456,esta_year='1995-3-23'),
# Hospital(Name='Relience Hospital',Phone_num=123456,esta_year='1995-3-23'),
# Hospital(Name='Applo Hospital',Phone_num=123456,esta_year='1995-3-23'),
# Hospital(Name='MMR Hospital',Phone_num=123456,esta_year='1995-3-23')]
# s = Hospital.objects.bulk_create(d)


# d = [Owner(Name='Riyanshi',hospi_id = 1),
# Owner(Name='Pooja',hospi_id = 2),
# Owner(Name='ABC',hospi_id = 3),
# Owner(Name='Lalit',hospi_id = 4),
# Owner(Name='Mohit',hospi_id = 5)]      

# s = Owner.objects.bulk_create(d)
# d = Department.objects.bulk_create([Department(Name='Nuerology',Total_Staff=10,hospi_id=1),
# Department(Name='Dertmatology',Total_Staff=12,hospi_id=1),
# Department(Name='Gynacology',Total_Staff = 6,hospi_id=2),
# Department(Name='X-ray',Total_Staff = 8,hospi_id=1),
# Department(Name='Orthology',Total_Staff = 8,hospi_id=2)])




# d = Doctor.objects.bulk_create([Doctor(Name='Riyanshi1',No_of_Doctor = 2,speciality="Pediatrition"),
# Doctor(Name='Riyanshi2',No_of_Doctor = 1,speciality="Pediatrition"),
# Doctor(Name='Riyanshi3',No_of_Doctor = 2,speciality="Pediatrition"),
# Doctor(Name='Riyanshi4',No_of_Doctor = 5,speciality="Pediatrition"),
# Doctor(Name='Riyanshi5',No_of_Doctor = 6,speciality="Pediatrition")])

# s = Doctor.objects.all()
# print(s.Name)
# d.save()

# Owner(Name='Pooja',hospi_id = 2),
# Owner(Name='ABC',hospi_id = 3),
# Owner(Name='Lalit',hospi_id = 4),
# Owner(Name='Mohit',hospi_id = 5)]

# s = Doctor.objects.get(Name='Mr. Mohit Borakhade')
# print(s.__dict__)

# print(s.Name , s.hospi_id)

# h = Hospital.objects.get(id=1)
# print(h.Name , h.Phone_num , h.esta_year)
# s.save()
# print(s)


O = Owner.objects.all().select_related('hospi').values_list('hospi__Name')
print(O)

