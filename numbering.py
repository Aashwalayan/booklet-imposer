def booklet_batches(total_pages, batch_size=32):
    if batch_size % 4 != 0:
        raise ValueError("Batch size must be divisible by 4.")

    padded_total = ((total_pages + batch_size - 1) // batch_size) * batch_size

    for start in range(1, padded_total + 1, batch_size):
        end = min(start + batch_size - 1, total_pages)

        batch_end = start + batch_size - 1

        pages = []

        left = start
        right = batch_end

        while left < right:
           
            pages.append((right, left))

            
            pages.append((left + 1, right - 1))

            left += 2
            right -= 2

        yield pages


total_pages = int(input("Enter total number of pages: "))

for batch_num, batch in enumerate(booklet_batches(total_pages), 1):
    print(f"\n=== BATCH {batch_num} ===")

    for sheet_num in range(0, len(batch), 2):
        front = batch[sheet_num]
        back = batch[sheet_num + 1]

        print(f"Sheet {(sheet_num // 2) + 1}: "
              f"Front [{front[0]}, {front[1]}]  "
              f"Back [{back[0]}, {back[1]}]")
