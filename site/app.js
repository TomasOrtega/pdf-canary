const form = document.querySelector("#canary-form");
const fileInput = document.querySelector("#pdf-file");
const factInput = document.querySelector("#canary-fact");
const status = document.querySelector("#status");
const result = document.querySelector("#result");
const canaryOutput = document.querySelector("#canary");
const download = document.querySelector("#download");
let downloadUrl;

function randomNumber() {
  const value = new Uint32Array(1);
  crypto.getRandomValues(value);
  return value[0] / 2 ** 32;
}

function canaryPageIndexes(pageCount) {
  const indexes = [];
  for (let index = 1; index < pageCount - 1; index += 2) {
    indexes.push(index);
  }
  return indexes.length ? indexes : Array.from({ length: pageCount }, (_, index) => index);
}

function outputName(inputName) {
  const stem = inputName.replace(/\.pdf$/i, "") || "document";
  return `${stem}-canary.pdf`;
}

function validateFact() {
  const invalid = !factInput.value.trim();
  factInput.setCustomValidity(invalid ? "Enter a slightly wrong fact." : "");
}

factInput.addEventListener("input", validateFact);
validateFact();

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  result.hidden = true;
  status.textContent = "Adding canaries…";

  try {
    const file = fileInput.files[0];
    const { PDFDocument, StandardFonts } = PDFLib;
    const pdf = await PDFDocument.load(await file.arrayBuffer());
    const font = await pdf.embedFont(StandardFonts.Helvetica);
    const canary = factInput.value.trim();
    const pages = pdf.getPages();

    for (const index of canaryPageIndexes(pages.length)) {
      const page = pages[index];
      const { width, height } = page.getSize();
      const size = Math.min(3, (width * 0.9 * 3) / font.widthOfTextAtSize(canary, 3));
      page.drawText(canary, {
        x: width * 0.05,
        y: height * (0.35 + randomNumber() * 0.35),
        size,
        font,
        opacity: 0,
      });
    }

    const bytes = await pdf.save();
    if (downloadUrl) {
      URL.revokeObjectURL(downloadUrl);
    }
    downloadUrl = URL.createObjectURL(new Blob([bytes], { type: "application/pdf" }));
    download.href = downloadUrl;
    download.download = outputName(file.name);
    canaryOutput.textContent = canary;
    result.hidden = false;
    status.textContent = "Done.";
  } catch {
    status.textContent = "Could not process this PDF. It may be encrypted or invalid.";
  }
});

window.addEventListener("beforeunload", () => {
  if (downloadUrl) {
    URL.revokeObjectURL(downloadUrl);
  }
});
