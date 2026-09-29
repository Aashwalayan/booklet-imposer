def booklet_batches(start_page, end_page, batch_size=32):
    if batch_size % 4 != 0:
        raise ValueError("Batch size must be divisible by 4.")

    total_pages = end_page - start_page + 1

    # Pad the final batch to a multiple of the batch size
    padded_total = (
        ((total_pages + batch_size - 1) // batch_size)
        * batch_size
    )

    for batch_start in range(
        start_page,
        start_page + padded_total,
        batch_size
    ):
        batch_end = batch_start + batch_size - 1

        pages = []

        left = batch_start
        right = batch_end

        while left < right:
            pages.append((right, left))
            pages.append((left + 1, right - 1))

            left += 2
            right -= 2

        yield pages


start_page = int(input("Enter starting page: "))
end_page = int(input("Enter ending page: "))
batch_size = int(input("Enter batch size: "))

for batch_num, batch in enumerate(
    booklet_batches(start_page, end_page, batch_size), 1
):
    print(f"\n=== BATCH {batch_num} ===")

    for sheet_num in range(0, len(batch), 2):
        front = batch[sheet_num]
        back = batch[sheet_num + 1]

        print(
            f"Sheet {(sheet_num // 2) + 1}: "
            f"Front [{front[0]}, {front[1]}]  "
            f"Back [{back[0]}, {back[1]}]"
        )
