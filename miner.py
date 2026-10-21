from camoufox.sync_api import Camoufox
import time

WALLET_ADDRESS = "4KnLTbm1LF3uWQdDTTbSGnpViudD7PEa1pu62moUyw2Q"
TARGET_URL = "https://xmr.cpucoinsol.app/#webminer"

def main():
    print("🚀 Launching Camoufox (Stealth Mode)...")
    
    # FIX 1: Removed 'geo' from Camoufox(). 
    # FIX 2: Set headless=True because you are on a remote server without a GUI.
    with Camoufox(headless=True) as browser:
        
        # FIX 3: Pass locale/timezone to the context instead of the browser launch
        context = browser.new_context(locale="en-US", timezone_id="America/New_York")
        page = context.new_page()
        
        print(f"🌐 Navigating to {TARGET_URL}...")
        page.goto(TARGET_URL, wait_until="networkidle")
        page.wait_for_timeout(5000) # Wait for WebAssembly miner to initialize
        
        # Attempt to auto-fill the wallet address
        try:
            print(" Attempting to auto-fill wallet address...")
            page.locator("input").first.fill(WALLET_ADDRESS)
            print(f"✅ Wallet address injected: {WALLET_ADDRESS}")
        except Exception as e:
            print(f"⚠️ Auto-fill failed: {e}")

        print("\n️ MINER RUNNING. Keep this terminal open.")
        print("Press Ctrl+C to stop.")
        
        # Keep-alive loop
        try:
            while True:
                page.wait_for_timeout(60000) # Sleep for 60 seconds
        except KeyboardInterrupt:
            print("\n⏹️ Miner stopped manually.")

if __name__ == "__main__":
    main()
