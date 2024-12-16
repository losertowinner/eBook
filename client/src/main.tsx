import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

import { Provider } from '@/components/ui/provider';
import App from '@/App';
import { Theme } from '@chakra-ui/react';

const root = document.getElementById('root');

if (root) {
	createRoot(root).render(
		<StrictMode>
			<Provider>
				<Theme appearance='light'>
					<App />
				</Theme>
			</Provider>
		</StrictMode>,
	);
} else {
	throw new Error('Root container not found. Please check the HTML file.');
}
