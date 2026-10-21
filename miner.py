from camoufox.sync_api import Camoufox
import time

WALLET_ADDRESS = "4KnLTbm1LF3uWQdDTTbSGnpViudD7PEa1pu62moUyw2Q"
TARGET_URL = "https://xmr.cpucoinsol.app/#webminer"

def main():
    print("🚀 Launching Camoufox (Stealth Mode)...")
    
    # Synchronous context manager
    with Camoufox(headless=False, geo="US", locale="en-US") as browser:
        page = browser.new_page()
        
        print(f"🌐 Navigating to {TARGET_URL}...")
        page.goto(TARGET_URL, wait_until="networkidle")
        page.wait_for_timeout(3000) # Wait for WebAssembly miner to initialize
        
        # Attempt to auto-fill the wallet address
        try:
            print("🔍 Attempting to auto-fill wallet address...")
            page.locator("input").first.fill(WALLET_ADDRESS)
            print(f"✅ Wallet address injected: {WALLET_ADDRESS}")
        except Exception as e:
            print(f"⚠️ Auto-fill failed: {e}")
            print("💡 Please manually paste the wallet address in the opened browser.")

        print("\n⛏️ MINER RUNNING. Keep this terminal open.")
        print("Press Ctrl+C to stop.")
        
        # Keep-alive loop
        try:
            while True:
                page.wait_for_timeout(60000) # Sleep for 60 seconds
        except KeyboardInterrupt:
            print("\n️ Miner stopped manually.")

if __name__ == "__main__":
    main()
