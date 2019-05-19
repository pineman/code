{
	i = 0
	while (++i <= $3) {
		printf("year %d: \t%.2f\n", i, $1 * (1+$2)^i)
	}

	for (i = 1; i <= $3; i++) {
		printf("year %d: \t%.2f\n", i, $1 * (1+$2)^i)
	}
}
