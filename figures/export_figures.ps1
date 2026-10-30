# Export each slide of the system-diagram deck as PNG and PDF into this folder.
# Needs PowerPoint (COM). Run from anywhere:
#   powershell -NoProfile -File export_figures.ps1                       # v7dk, the current deck
#   powershell -NoProfile -File export_figures.ps1 -Deck "system_diagrams v6dk.pptx" -Out "v6"
param(
    [string]$Deck = "system_diagrams v7dk.pptx",
    [string]$Out = "."
)
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$src = Join-Path $here $Deck
$out = (Resolve-Path (Join-Path $here $Out)).Path
# slide order: legend, Fig. 1, 2, 3, 4, 4a, 4b
$names = @("legend", "fig1", "fig2", "fig3", "fig4", "fig4a", "fig4b")

$app = New-Object -ComObject PowerPoint.Application
$pres = $app.Presentations.Open($src, $true, $false, $false)
try {
    for ($i = 1; $i -le $pres.Slides.Count; $i++) {
        $name = $names[$i - 1]
        $pres.Slides.Item($i).Export((Join-Path $out "$name.png"), "PNG", 2667, 1500)
        $pres.PrintOptions.Ranges.ClearAll() | Out-Null
        $range = $pres.PrintOptions.Ranges.Add($i, $i)
        # ExportAsFixedFormat(Path, ppFixedFormatTypePDF=2, Intent=ppFixedFormatIntentPrint=1, FrameSlides=0,
        #   HandoutOrder=1, OutputType=ppPrintOutputSlides=1, PrintHiddenSlides=0, PrintRange, RangeType=ppPrintSlideRange=4)
        $pres.ExportAsFixedFormat((Join-Path $out "$name.pdf"), 2, 1, 0, 1, 1, 0, $range, 4)
        Write-Output ("{0,-6} -> {1}.png, {1}.pdf" -f $name, $name)
    }
} finally {
    $pres.Close()
    $app.Quit()
}
