import { Component, signal } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'fn-root',
  imports: [RouterOutlet, MatSidenavModule, MatButtonModule, MatIconModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'financier';

  isSideNavOpen = signal<boolean>(false);

  toggleSideNav() {
    this.isSideNavOpen.update((currentStatus) => !currentStatus);
  }
}
