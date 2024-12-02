<script lang="ts">
	import type { TransactionRowType } from '$lib/app/types';
	import Upload from '$lib/components/Upload.svelte';
	import TransactionTable from '$lib/components/TransactionTable.svelte';
	import { LightSwitch } from '@skeletonlabs/skeleton';

	let file: File | null;
	let transactions: TransactionRowType[] = [];

	const fileUploadHandler = (files: FileList) => {
		file = files.item(0);
		for (let i = 0; i < 50; i++) {
			let transaction: TransactionRowType = {
				accountType: 'Visa',
				accountNumber: '111-111-111',
				transactionDate: new Date(),
				cost: [-200, 15, 35][i % 3],
				description: ['PERSONAL LOAN', 'NETFLIX SEATTLE VALLEY I.', 'SOBEYS INC'][i % 3],
				category: ['Car', 'Entertainment', 'Groceries'][i % 3]
			};
			transactions.push(transaction);
		}
	};
</script>

<div class="flex flex-col w-screen h-screen">
	<div class="flex justify-start p-4">
		<LightSwitch />
	</div>

	{#if file != null}
		<div class="flex-grow flex flex-col items-center justify-center w-screen mb-4">
			<div class="w-3/4 mb-6">
				<h1 class="text-4xl font-bold">Transactions</h1>
			</div>

			<div class="flex-grow flex justify-center w-screen">
				<TransactionTable data={transactions} />
			</div>
		</div>
	{:else}
		<div class="flex-grow flex justify-center items-center w-screen">
			<Upload fileHandler={fileUploadHandler} />
		</div>
	{/if}
</div>
