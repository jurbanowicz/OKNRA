SIZE = 2048

PAPI = -I/usr/local/include -L/usr/local/lib -lpapi

test:
	gcc chol_1.c -o chol_1 -lm $(PAPI)
	./chol_1 $(SIZE) 2

compile_all:
	gcc chol_1.c -o chol_1 -lm $(PAPI)
	gcc chol_2.c -o chol_2 -lm $(PAPI)
	gcc chol_3.c -o chol_3 -lm $(PAPI)
	gcc chol_4.c -o chol_4 -lm $(PAPI)
	gcc chol_5.c -o chol_5 -lm $(PAPI)
	gcc chol_6.c -o chol_6 -lm -mavx $(PAPI)

run_all:
	make compile_all
	./run_all.sh

run:
	echo "version = '$(VERSION)'" > results/result_$(VERSION).txt
	./$(VERSION) 100 2 >> results/result_$(VERSION).txt
	./$(VERSION) 200 2 >> results/result_$(VERSION).txt
	./$(VERSION) 300 2 >> results/result_$(VERSION).txt
	./$(VERSION) 400 2 >> results/result_$(VERSION).txt
	./$(VERSION) 500 2 >> results/result_$(VERSION).txt
	./$(VERSION) 800 2 >> results/result_$(VERSION).txt
	./$(VERSION) 1000 2 >> results/result_$(VERSION).txt
	./$(VERSION) 1300 2 >> results/result_$(VERSION).txt
	./$(VERSION) 1600 2 >> results/result_$(VERSION).txt
	./$(VERSION) 2000 2 >> results/result_$(VERSION).txt
	

test_all:
	gcc chol_1.c -o chol_1 -lm $(PAPI)
	./chol_1 $(SIZE) 2 > results/result1.txt

	gcc chol_2.c -o chol_2 -lm $(PAPI)
	./chol_2 $(SIZE) 2 > results/result2.txt

	gcc chol_3.c -o chol_3 -lm $(PAPI)
	./chol_3 $(SIZE) 2 > results/result3.txt

	gcc chol_4.c -o chol_4 -lm $(PAPI)
	./chol_4 $(SIZE) 2 > results/result4.txt

	gcc chol_5.c -o chol_5 -lm $(PAPI)
	./chol_5 $(SIZE) 2 > results/result5.txt

	gcc chol_6.c -o chol_6 -lm -mavx $(PAPI)
	./chol_6 $(SIZE) 2 > results/result6.txt
