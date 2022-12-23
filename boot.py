
from sdcardio import SDCard
from storage import mount
from busio import SPI
import board

spi = SPI(
    clock=board.GP18,
    MISO=board.GP16,
    MOSI=board.GP19
)

sdc = SDCard(spi,board.GP21)
mount(sdc,"/sdc/")
