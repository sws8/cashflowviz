<script lang="ts">
	import { FileDropzone } from '@skeletonlabs/skeleton';
	import Icon from '@iconify/svelte';
	import { upload_handler } from '$lib/services/upload';

	async function onChangeHandler(e: Event) {
		upload_handler();
	};
</script>

<FileDropzone class="w-[624px]" name="files" on:click={onChangeHandler}>
	<div class="justify-center" slot="lead">
		<Icon class="text-5xl w-screen" icon="mdi:file-upload" />
	</div>
	<svelte:fragment slot="meta">Upload an Excel or CVS.</svelte:fragment>
</FileDropzone>
