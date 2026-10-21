import asyncio
from camoufox import Camoufox

WALLET_ADDRESS = "4KnLTbm1LF3uWQdDTTbSGnpViudD7PEa1pu62moUyw2Q"
TARGET_URL = "https://xmr.cpucoinsol.app/#webminer"

async def main():
    print("🚀 Launching Camoufox (Stealth Mode)...")
    
    # Launch Camoufox. Set headless=False to see the browser, True for VPS
    async with Camoufox(headless=False, geo="US", locale="en-US") as browser:
        page = await browser.new_page()
        
        print(f"🌐 Navigating to {TARGET_URL}...")
        await page.goto(TARGET_URL, wait_until="networkidle")
        await page.wait_for_timeout(3000) # Wait for WebAssembly miner to initialize
        
        # Attempt to auto-fill the wallet address
        try:
            print("🔍 Attempting to auto-fill wallet address...")
            # Target the first visible input field (adjust if the site uses specific IDs)
            await page.locator("input").first.fill(WALLET_ADDRESS)
            print(f"✅ Wallet address injected: {WALLET_ADDRESS}")
        except Exception as e:
            print(f"⚠️ Auto-fill failed: {e}")
            print("💡 Please manually paste the wallet address in the opened browser.")

        print("\n⛏️ MINER RUNNING. Keep this terminal open.")
        print("Press Ctrl+C to stop.")
        
        # Keep-alive loop
        try:
            while True:
                await asyncio.sleep(60)
                # Optional: Prevent session timeout by subtle interaction
                # await page.mouse.move(100, 100)
        except KeyboardInterrupt:
            print("\n⏹️ Miner stopped manually.")

if __name__ == "__main__":
    asyncio.run(main())
