dob(john, date(1990, 5, 15)).
dob(emma, date(1985, 9, 28)).
dob(michael, date(1998, 2, 10)).
dob(sophia, date(2002, 11, 3)).
get_dob(Person, DateOfBirth) :- dob(Person, DateOfBirth).
born_before_year(Person, Year) :- dob(Person, date(Y, _, _)),Y < Year.
