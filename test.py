#!/usr/bin/env python3
"""
Simple test script for EchoFund API
Run this after starting the server to verify all endpoints work.
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing health check...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_add_transaction():
    """Test adding a transaction"""
    print("➕ Testing add transaction...")
    data = {
        "description": "Starbucks Coffee",
        "amount": 5.50,
        "emotional_context": "stressful day"
    }
    response = requests.post(f"{BASE_URL}/api/transactions/", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()
    return response.json().get("transaction", {}).get("id")

def test_get_transactions():
    """Test getting all transactions"""
    print("📋 Testing get transactions...")
    response = requests.get(f"{BASE_URL}/api/transactions/")
    print(f"Status: {response.status_code}")
    print(f"Found {len(response.json())} transactions")
    print()

def test_behavioral_profile():
    """Test getting behavioral profile"""
    print("🧠 Testing behavioral profile...")
    response = requests.get(f"{BASE_URL}/api/behavioral-profile/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_simulate():
    """Test simulation"""
    print("⏰ Testing simulation...")
    data = {
        "target_category": "Impulse/Coffee",
        "reduction_amount": 3.00,
        "months_to_simulate": 12
    }
    response = requests.post(f"{BASE_URL}/api/simulate/", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_summary():
    """Test summary endpoint"""
    print("📊 Testing summary...")
    response = requests.get(f"{BASE_URL}/api/summary/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def main():
    print("=" * 50)
    print("🧪 EchoFund API Test Suite")
    print("=" * 50)
    print()
    
    try:
        test_health_check()
        
        # Add some sample transactions
        print("Adding sample transactions...")
        sample_transactions = [
            {"description": "Starbucks Coffee", "amount": 5.50, "emotional_context": "morning rush"},
            {"description": "Uber ride", "amount": 12.00},
            {"description": "Amazon shopping", "amount": 45.99, "emotional_context": "impulse buy"},
            {"description": "Restaurant dinner", "amount": 35.00},
            {"description": "Groceries", "amount": 85.50},
        ]
        
        for txn in sample_transactions:
            requests.post(f"{BASE_URL}/api/transactions/", json=txn)
        
        test_get_transactions()
        test_behavioral_profile()
        test_simulate()
        test_summary()
        
        print("=" * 50)
        print("✅ All tests completed!")
        print("=" * 50)
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server.")
        print("   Make sure the backend is running on http://localhost:8000")
        print("   Start it with: uvicorn main:app --reload")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
