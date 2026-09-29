# Booklet Printer

A simple Python utility that generates **booklet-style page ordering** for duplex printing.

It takes a starting page, ending page, and batch size, then calculates which pages should appear together on the front and back of each physical sheet.

## Features

* Specify any starting and ending page
* Choose any batch size divisible by 4
* Automatically splits large documents into batches
* Generates front/back page pairs for booklet printing
* Automatically handles incomplete final batches by continuing with the required extra page numbers
* No external dependencies

## How It Works

For a normal 32-page booklet, the pages are arranged like:

```text
Front: 32, 1    → Back: 2, 31
Front: 30, 3    → Back: 4, 29
Front: 28, 5    → Back: 6, 27
...
Front: 18, 15   → Back: 16, 17
```

After printing, folding, and stacking the sheets, the pages appear in normal reading order.

## Usage

Run:

```bash
python booklet.py
```

You'll be asked for:

```text
Enter starting page: 300
Enter ending page: 390
Enter batch size: 32
```

The program then outputs something like:

```text
=== BATCH 1 ===

Sheet 1: Front [331, 300]  Back [301, 330]
Sheet 2: Front [329, 302]  Back [303, 328]
Sheet 3: Front [327, 304]  Back [305, 326]
...
```

## Batch Size

The batch size must be divisible by **4** because every physical sheet contains four page positions:

* 2 pages on the front
* 2 pages on the back

Examples of valid batch sizes:

```text
4
8
16
32
64
128
```

## Example

For:

```text
Starting page: 300
Ending page: 390
Batch size: 32
```

The program creates batches covering:

```text
300–331
332–363
364–391
```

The final batch is extended as necessary to complete the booklet structure.

## Requirements

* Python 3.x

No additional packages are required.

## Future Plans

Possible future improvements:

* Generate print-ready PDFs automatically
* Upload a PDF and automatically rearrange its pages
* Support Word documents
* Add a graphical/web interface
* Add different binding directions
* Add paper-size and printer settings
* Preview the final booklet layout

## License

This project is currently intended as a personal/experimental project.
