<script lang="ts">
	import { FileDropzone } from '@skeletonlabs/skeleton';
	import Icon from '@iconify/svelte';

	export let fileHandler;
	let fileList: FileList;

	const onChangeHandler = (e: Event) => {
		if (fileList.item(0)?.type === 'text/csv') fileHandler(fileList);
	};
</script>

<FileDropzone class="w-[624px]" name="files" bind:files={fileList} on:change={onChangeHandler}>
	<div class="justify-center" slot="lead">
		<Icon class="text-5xl w-screen" icon="mdi:file-upload" />
	</div>
	<svelte:fragment slot="meta">Upload an Excel or CVS.</svelte:fragment>
</FileDropzone>
