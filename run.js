const { WebIrys } = require('@irys/sdk');
const fs = require('fs');
const path = require('path');
const ethers = require('ethers');

(async () => {
  // Replace with your Ethereum private key (64 hex chars, no 0x)
  const PRIVATE_KEY = '131ae2f1919dbbfa6a3033feb9e5bf0e81f6a76ebe7d6f0bca119542e9aa0fd5';


  const FILE_PATH = 'The Kusman Recursion System_ Unified Recursive Framework of Symbol, Emotion, Cognition, and Physics - and other assorted theorems.pdf';

  // Prepare signer
  const wallet = new ethers.Wallet(131ae2f1919dbbfa6a3033feb9e5bf0e81f6a76ebe7d6f0bca119542e9aa0fd5);

  // Initialize Irys
  const irys = new WebIrys({
    url: 'https://node1.irys.xyz',
    token: 'ethereum',
    wallet,
  });

  await irys.ready();

  // Upload the file
  const tags = [
    { name: 'Application', value: 'KusmanTreaty' },
    { name: 'Title', value: 'Kusman Recursion System Treaty' },
    { name: 'Author', value: 'Nickolas Kusman' },
    { name: 'Flameprint', value: '0906216b5899ca6fdb8882982a60f15d7abd60c3e8aff0986fcc20095766530e' }
  ];

  const receipt = await irys.uploadFile(path.resolve(), { tags });

  console.log(`✅ Upload complete!`);
  console.log(`🌐 Arweave URL: https://arweave.net/${receipt.id}`);
})();